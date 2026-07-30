import grpc
import logging
import atexit
import rs3.generatedFiles.ClientService_pb2_grpc as ClientService_pb2_grpc
import rs3.generatedFiles.ClientService_pb2 as ClientService_pb2

class Client:
    def __init__(self, port):
        self.compatibleProgramVersion = "4.043"
        self.connection = self._establishConnection(port)
        self.logger = logging.getLogger('Rocscience.RS3')
        atexit.register(self.closeConnection)
        
        clientService = ClientService_pb2_grpc.ClientServiceStub(self.channel)
        request = ClientService_pb2._GetProgramVersionRequest()
        versionCompatible = self.callFunction(clientService._GetProgramVersion, request).result
        if self.compatibleProgramVersion != versionCompatible:
            self.closeConnection()
            raise RuntimeError(f"""
					  Library version is not compatible with the program version. 
					  Please ensure the versions match by installing the correct version of the library or program. 
					  Library version: {self.compatibleProgramVersion} Program version: find in help->about.
					  """
					  )
        
    def _establishConnection(self, port):
        self.channel = grpc.insecure_channel(f"localhost:{port}")

    def closeConnection(self):
        if self.channel:
            self.channel.close()
            self.channel = None

    def callFunction(self, function, request):
        try:
            response, call = function.with_call(request)
            self._logMessages(call)
            return response
        except grpc.RpcError as e:
            self.logger.exception("An exception was raised from the application.")
            raise
            
    def _logMessages(self, call):
        if not call:
            return
        
        for key, value in call.trailing_metadata():
            # Decode bytes to string if needed
            if isinstance(value, bytes):
                value = value.decode('utf-8')
            
            if key == "warning-bin":
                self.logger.warning(value)
            if key == "info-bin":
                self.logger.info(value)
            if key == "debug-bin":
                self.logger.debug(value)
