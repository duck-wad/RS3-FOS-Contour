"""Connect to RS3, reusing a live scripting server / open model when possible."""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from rs3.Model import Model
    from rs3.RS3Modeler import RS3Modeler


@dataclass
class RS3Session:
    """Active RS3 scripting connection and ownership flags for cleanup."""

    modeler: "RS3Modeler"
    model: "Model"
    model_path: Path
    port: int
    started_application: bool
    opened_model: bool
    model_was_already_open: bool

    def close(self, *, keep_open: bool = False) -> None:
        """
        Release resources we own.

        - Never close a model the user already had open.
        - Never quit RS3 unless this session started it (and keep_open is False).
        """
        if keep_open:
            return

        if self.opened_model and not self.model_was_already_open:
            try:
                self.model.close(False)
            except Exception as exc:  # noqa: BLE001 - best-effort cleanup
                print(f"Warning: model.close failed: {exc}", flush=True)

        if self.started_application:
            try:
                self.modeler.closeProgram(saveModels=False)
            except Exception as exc:  # noqa: BLE001
                print(f"Warning: closeProgram failed: {exc}", flush=True)


def _call_with_timeout(fn: Callable, timeout_s: float, label: str):
    """Run ``fn`` in a worker thread; raise TimeoutError if it exceeds ``timeout_s``."""
    with ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(fn)
        try:
            return future.result(timeout=timeout_s)
        except FuturesTimeout as exc:
            raise TimeoutError(
                f"Timed out after {timeout_s:g}s while {label}. "
                "RS3 may be busy or the scripting call is stuck."
            ) from exc


def _open_model_with_timeout(
    modeler: "RS3Modeler",
    path_str: str,
    *,
    already_open: bool,
    timeout_s: float,
    progress_callback,
) -> "Model":
    """
    Open / attach to a model without relying on RS3's infinite openFile wait.

    RS3Modeler.openFile polls ``_isViewLoaded`` forever with no timeout. When the
    view is already loaded we skip that loop entirely.
    """
    from rs3.Model import Model
    from rs3.RS3Modeler import RS3ModelerBase

    if already_open:
        project_id = _call_with_timeout(
            lambda: RS3ModelerBase.openFile(modeler, path_str),
            timeout_s,
            f"attaching to already-open model ({path_str})",
        )
        return Model(modeler._client, project_id)

    project_id = _call_with_timeout(
        lambda: RS3ModelerBase.openFile(modeler, path_str),
        timeout_s,
        f"requesting open of {path_str}",
    )

    deadline = time.monotonic() + timeout_s
    while True:
        loaded = _call_with_timeout(
            lambda: modeler._isViewLoaded(path_str),
            min(30.0, max(1.0, deadline - time.monotonic())),
            "checking whether the model view finished loading",
        )
        if loaded:
            return Model(modeler._client, project_id)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(
                f"Timed out after {timeout_s:g}s waiting for RS3 to finish "
                f"loading {path_str}."
            )
        progress_callback(
            f"Waiting for model view to load... ({remaining:.0f}s remaining)"
        )
        time.sleep(0.5)


def _server_is_running(port: int) -> bool:
    """
    Return True only if the RS3 scripting server answers a ping.

    RS3Modeler._isServerRunning raises on connection refused instead of
    returning False, so we treat any failure as "not running".
    """
    from rs3.RS3Modeler import RS3Modeler

    try:
        return bool(RS3Modeler._isServerRunning(port))
    except Exception:  # noqa: BLE001 - connection refused / unavailable
        return False


def connect_model(
    model_path: Path,
    *,
    port: int = 60064,
    force_no_start: bool = False,
    open_timeout_s: float = 180.0,
    progress_callback=print,
) -> RS3Session:
    """
    Attach to RS3 and return a handle to ``model_path``.

    Behavior
    --------
    1. If a scripting server is already listening on ``port``, connect to it.
    2. Otherwise start RS3 with scripting enabled (unless ``force_no_start``).
    3. If the model view is already loaded, reuse it (no reload wait).
    4. Otherwise open the file, with a hard timeout.
    """
    from .rs3_bootstrap import ensure_rs3_protobuf_imports

    ensure_rs3_protobuf_imports()

    from rs3.RS3Modeler import RS3Modeler

    path = model_path.resolve()
    path_str = str(path)

    server_running = _server_is_running(port)
    started_application = False

    if server_running:
        progress_callback(
            f"RS3 scripting server already running on port {port}; attaching..."
        )
    elif force_no_start:
        raise RuntimeError(
            f"No RS3 scripting server on port {port}, and --no-start was set.\n"
            "Either start RS3 with scripting enabled, omit --no-start so this "
            "app can launch RS3, or open RS3 via RS3Modeler.startApplication."
        )
    else:
        progress_callback(
            f"No scripting server on port {port}. "
            "Starting RS3 with scripting enabled..."
        )
        try:
            RS3Modeler.startApplication(port=port)
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(
                f"Could not start RS3 scripting server on port {port}.\n"
                f"Details: {exc}\n\n"
                "If RS3 is already open without scripting, close it and try "
                "again so a scripting-enabled instance can start."
            ) from exc
        started_application = True
        # Wait briefly for the server to accept connections after process start.
        deadline = time.monotonic() + max(30.0, open_timeout_s)
        while not _server_is_running(port):
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"RS3 started but the scripting server on port {port} "
                    "never became ready."
                )
            time.sleep(0.5)
        progress_callback(f"Scripting server ready on port {port}.")

    modeler = RS3Modeler(port=port)

    already_open = False
    try:
        already_open = bool(
            _call_with_timeout(
                lambda: modeler._isViewLoaded(path_str),
                min(30.0, open_timeout_s),
                "checking if the model is already open",
            )
        )
    except Exception as exc:  # noqa: BLE001 - private helper; fall through to open
        progress_callback(f"Could not check if model is open ({exc}); opening file...")

    if already_open:
        progress_callback(f"Model already open; reusing: {path}")
    else:
        progress_callback(f"Opening {path}...")

    model = _open_model_with_timeout(
        modeler,
        path_str,
        already_open=already_open,
        timeout_s=open_timeout_s,
        progress_callback=progress_callback,
    )

    return RS3Session(
        modeler=modeler,
        model=model,
        model_path=path,
        port=port,
        started_application=started_application,
        opened_model=True,
        model_was_already_open=already_open,
    )
