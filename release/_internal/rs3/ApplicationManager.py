import subprocess
import time
from multiprocessing.connection import Listener
from logging import Logger

class ApplicationManager:
    minimumPort = 49152
    maximumPort = 65535
    defaultTimeout = 120
    def startApplication(self, pathToExecutable : str, port : int, isServerRunning : callable, logger : Logger, timeout : float = defaultTimeout ):
        """
        Starts the application specified by pathToExecutable and starts the python server on the given port. 
        Returns when the server is ready to accept requests.
        Throws TimeoutError exception if the server is not ready within that time.

        Args:
            pathToExecutable: the full path to the executable of the application you want to start.
            port: the port number you want the python server to bind to.
            isServerRunning: a callable that returns True if the server is ready to accept requests.
            logger: a logger object. It will be disabled while trying to connect to the server.
            timeout: time in seconds before we stop trying to start the application
        
        Raises:
        	ValueError: Port range must be between 49152 and 65535, otherwise ValueError is raised
		    TimeoutError: if timeout is provided, raises TimeoutError if not able to connect to the server within that time.
        """
        if port < self.minimumPort or port > self.maximumPort:
            msg = f"port must be in the range {self.minimumPort} to {self.maximumPort}"
            logger.error(msg)
            raise ValueError(msg)
        
        if not self._isPortAvailable(port):
            msg = f"port number {port} is occupied. Please choose another port."
            logger.error(msg)
            raise RuntimeError(msg)

        logger.info(f"Attempting to start the application at {pathToExecutable} and binding server to port {port}...")
        subprocess.Popen([f"{pathToExecutable}", "-startScriptingServer", f"{port}"], start_new_session = True, creationflags=subprocess.DETACHED_PROCESS)

        self._tryToConnectToServer(port, isServerRunning, timeout, logger)
       

    def _isPortAvailable(self, port):
        portAvailable = False
        listener = None
        try:
            listener = Listener(('localhost', port), 'AF_INET')
            portAvailable = True
        except Exception:
            portAvailable = False
        
        if listener:
            listener.close()

        return portAvailable

    def _tryToConnectToServer(self, port : int, isServerRunning : callable, timeout, logger : Logger):

        startTime = time.time()
        serverIsRunning = False

        while not serverIsRunning:
            if timeout:
                if (time.time() - startTime) > timeout:
                    msg = "The application did not start within the given timeout time."
                    logger.error(msg)
                    raise TimeoutError(msg)
            try:
                logger.debug("Trying to connect to the server...")
                logger.disabled = True
                isServerRunning(port)
            except Exception as e:
                continue
            finally:
                logger.disabled = False
            serverIsRunning = True
            logger.debug("connectied!")