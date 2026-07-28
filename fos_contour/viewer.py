"""
Qt + PyVista FoS contour viewer with FLAC-style solid zone coloring.

Controls for criterion, stage, mode, and limit live in this window.
"""

from __future__ import annotations

import traceback
from pathlib import Path
from typing import Any

import numpy as np

from .criteria import Criterion, FailureMode, parse_criterion, parse_failure_mode
from .dataset import (
    ContourDataset,
    build_fos_mesh,
    compute_local_fos_array,
    histories_to_dataset,
)
from .export import suggest_limit


def _require_qt_pyvista():
    try:
        from PySide6 import QtCore, QtWidgets
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "PySide6 is required for the FoS viewer. Install with:\n"
            "  pip install PySide6 pyvista pyvistaqt\n"
        ) from exc
    try:
        import pyvista as pv
        from pyvistaqt import QtInteractor
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "PyVista / pyvistaqt are required. Install with:\n"
            "  pip install pyvista pyvistaqt\n"
        ) from exc
    return QtCore, QtWidgets, pv, QtInteractor


def default_limit_range(
    dataset: ContourDataset, initial_limit: float
) -> tuple[float, float]:
    finite = dataset.values[np.isfinite(dataset.values)]
    if finite.size == 0:
        return (initial_limit * 0.1, initial_limit * 10.0)
    lo = max(float(np.percentile(finite, 1)), np.finfo(float).tiny)
    hi = float(np.percentile(finite, 99))
    if hi <= lo:
        hi = lo * 10.0
    lo = min(lo, initial_limit * 0.2)
    hi = max(hi, initial_limit * 2.0)
    return lo, hi


def fos_clim(local_fos: np.ndarray, dataset: ContourDataset) -> tuple[float, float]:
    finite = local_fos[np.isfinite(local_fos)]
    if finite.size == 0:
        return (1.0, dataset.max_srf)
    return (float(np.min(finite)), float(np.max(finite)))


class ExtractWorker:
    """Background extract so the Qt UI stays responsive."""

    def __init__(self, parent, fn, on_done, on_error, on_log) -> None:
        QtCore, _, _, _ = _require_qt_pyvista()

        class _Thread(QtCore.QThread):
            log = QtCore.Signal(str)
            finished_ok = QtCore.Signal(object)
            failed = QtCore.Signal(str)

            def run(self_inner) -> None:  # noqa: N805
                try:
                    def progress(msg: str) -> None:
                        self_inner.log.emit(str(msg))

                    result = fn(progress)
                    self_inner.finished_ok.emit(result)
                except Exception:  # noqa: BLE001
                    self_inner.failed.emit(traceback.format_exc())

        self.thread = _Thread(parent)
        self.thread.log.connect(on_log)
        self.thread.finished_ok.connect(on_done)
        self.thread.failed.connect(on_error)

    def start(self) -> None:
        self.thread.start()


class FoSMainWindow:
    """Single-window FoS contour application."""

    def __init__(
        self,
        *,
        model: Path | None = None,
        port: int = 60064,
        stage: int = 1,
        criterion: str = "total_displacement",
        mode: str = "absolute",
        no_start: bool = False,
        auto_extract: bool = False,
    ) -> None:
        QtCore, QtWidgets, pv, QtInteractor = _require_qt_pyvista()
        self.QtCore = QtCore
        self.QtWidgets = QtWidgets
        self.pv = pv
        self.QtInteractor = QtInteractor

        self.port = port
        self.no_start = no_start
        self.dataset: ContourDataset | None = None
        self.suggestions: dict[str, float] | None = None
        self._mesh_actor = None
        self._worker: ExtractWorker | None = None
        self._updating_controls = False

        self.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("RS3 Local FoS Contour Viewer")
        self.window.resize(1280, 800)

        central = QtWidgets.QWidget()
        self.window.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # --- toolbar ---
        bar = QtWidgets.QHBoxLayout()
        self.model_edit = QtWidgets.QLineEdit(
            str(model.resolve()) if model else ""
        )
        browse = QtWidgets.QPushButton("Browse…")
        browse.clicked.connect(self._browse)
        self.extract_btn = QtWidgets.QPushButton("Extract from RS3")
        self.extract_btn.clicked.connect(self._start_extract)
        bar.addWidget(QtWidgets.QLabel("Model"))
        bar.addWidget(self.model_edit, stretch=1)
        bar.addWidget(browse)
        bar.addWidget(self.extract_btn)
        layout.addLayout(bar)

        opts = QtWidgets.QHBoxLayout()
        self.port_spin = QtWidgets.QSpinBox()
        self.port_spin.setRange(49152, 65535)
        self.port_spin.setValue(port)

        self.stage_spin = QtWidgets.QSpinBox()
        self.stage_spin.setRange(1, 999)
        self.stage_spin.setValue(stage)

        self.criterion_combo = QtWidgets.QComboBox()
        self.criterion_combo.addItems(["total_displacement", "max_shear_strain"])
        idx = self.criterion_combo.findText(criterion)
        if idx >= 0:
            self.criterion_combo.setCurrentIndex(idx)

        self.mode_combo = QtWidgets.QComboBox()
        self.mode_combo.addItems(["absolute", "incremental"])
        idx = self.mode_combo.findText(mode)
        if idx >= 0:
            self.mode_combo.setCurrentIndex(idx)

        self.limit_spin = QtWidgets.QDoubleSpinBox()
        self.limit_spin.setDecimals(8)
        self.limit_spin.setRange(1e-12, 1e12)
        self.limit_spin.setSingleStep(1e-4)
        self.limit_spin.setValue(0.001)

        self.limit_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.limit_slider.setRange(0, 1000)
        self.limit_slider.setValue(500)

        for label, widget in (
            ("Port", self.port_spin),
            ("Stage", self.stage_spin),
            ("Criterion", self.criterion_combo),
            ("Mode", self.mode_combo),
            ("Limit", self.limit_spin),
        ):
            opts.addWidget(QtWidgets.QLabel(label))
            opts.addWidget(widget)
        opts.addWidget(self.limit_slider, stretch=1)
        layout.addLayout(opts)

        self.criterion_combo.currentTextChanged.connect(self._on_criterion_or_stage)
        self.stage_spin.valueChanged.connect(self._on_criterion_or_stage)
        self.mode_combo.currentTextChanged.connect(self._on_mode_changed)
        self.limit_spin.valueChanged.connect(self._on_limit_spin)
        self.limit_slider.valueChanged.connect(self._on_limit_slider)

        # --- 3D view ---
        self.plotter = QtInteractor(central)
        layout.addWidget(self.plotter.interactor, stretch=1)
        self.plotter.set_background("white")
        self.plotter.add_axes(line_width=2)

        self.log = QtWidgets.QPlainTextEdit()
        self.log.setReadOnly(True)
        self.log.setMaximumHeight(120)
        layout.addWidget(self.log)

        self.status = QtWidgets.QStatusBar()
        self.window.setStatusBar(self.status)
        self.status.showMessage(
            "Load a computed .rs3v3 and click Extract from RS3."
        )

        if auto_extract and model is not None:
            QtCore.QTimer.singleShot(250, self._start_extract)

    def _log(self, message: str) -> None:
        self.log.appendPlainText(message)

    def _browse(self) -> None:
        path, _ = self.QtWidgets.QFileDialog.getOpenFileName(
            self.window,
            "Select RS3 model",
            "",
            "RS3 model (*.rs3v3);;All files (*.*)",
        )
        if path:
            self.model_edit.setText(path)

    def _start_extract(self) -> None:
        if self._worker is not None and self._worker.thread.isRunning():
            return
        model = Path(self.model_edit.text().strip())
        if not model.exists():
            self.QtWidgets.QMessageBox.critical(
                self.window, "Model not found", f"File does not exist:\n{model}"
            )
            return

        self.extract_btn.setEnabled(False)
        self.status.showMessage("Extracting SSR histories from RS3…")
        self._log(f"Extracting {model} …")

        port = int(self.port_spin.value())
        stage = int(self.stage_spin.value())
        criterion = parse_criterion(self.criterion_combo.currentText())
        failure_mode = parse_failure_mode(self.mode_combo.currentText())
        no_start = self.no_start

        def work(progress) -> tuple[ContourDataset, dict[str, float], float]:
            from .rs3_extract import extract_nodal_histories
            from .session import connect_model

            session = connect_model(
                model,
                port=port,
                force_no_start=no_start,
                progress_callback=progress,
            )
            try:
                trials, histories, elements = extract_nodal_histories(
                    session.model,
                    criterion=criterion,
                    stage_number=stage,
                    surface_only=False,
                    include_elements=True,
                    progress_callback=progress,
                )
                suggestions = suggest_limit(
                    trials, histories, failure_mode=failure_mode
                )
                dataset = histories_to_dataset(
                    trials,
                    histories,
                    criterion=criterion,
                    failure_mode=failure_mode,
                    stage_number=stage,
                    model_path=str(model),
                    elements=elements,
                )
                initial_limit = float(suggestions["suggested"])
                for key, value in suggestions.items():
                    progress(f"  {key}: {value:g}")
                progress("Extract complete — building contour view…")
                return dataset, suggestions, initial_limit
            finally:
                # Never close the model or quit RS3 from the viewer.
                # Scripted model.close / closeProgram can crash RS3's UI
                # (Eyeshot RemoveView). Leave the session running.
                try:
                    session.close(keep_open=True)
                except Exception as exc:  # noqa: BLE001
                    progress(f"Warning during session cleanup: {exc}")

        self._worker = ExtractWorker(
            self.window,
            work,
            on_done=self._on_extract_done,
            on_error=self._on_extract_error,
            on_log=self._log,
        )
        self._worker.start()

    def _on_extract_done(self, payload: object) -> None:
        try:
            dataset, suggestions, initial_limit = payload  # type: ignore[misc]
            self.dataset = dataset
            self.suggestions = suggestions
            self.extract_btn.setEnabled(True)
            self._updating_controls = True
            try:
                lo, hi = default_limit_range(dataset, initial_limit)
                self.limit_spin.blockSignals(True)
                self.limit_slider.blockSignals(True)
                self.limit_spin.setRange(lo, hi)
                self.limit_spin.setSingleStep((hi - lo) / 200.0)
                self.limit_spin.setValue(initial_limit)
                self._sync_slider_from_limit(initial_limit)
            finally:
                self.limit_spin.blockSignals(False)
                self.limit_slider.blockSignals(False)
                self._updating_controls = False
            self._render_dataset(initial_limit)
            self.status.showMessage(
                f"Ready — {dataset.n_nodes} nodes, {dataset.n_elements} elements. "
                "Adjust limit / mode live; criterion & stage re-extract."
            )
        except Exception:  # noqa: BLE001
            self.extract_btn.setEnabled(True)
            self.status.showMessage("Extract finished but rendering failed.")
            self._log(traceback.format_exc())
            self.QtWidgets.QMessageBox.critical(
                self.window,
                "Render failed",
                "Data was extracted but the contour view could not be built.\n\n"
                + traceback.format_exc(),
            )

    def _on_extract_error(self, message: str) -> None:
        self.extract_btn.setEnabled(True)
        self.status.showMessage("Extract failed.")
        self._log(message)
        pretty = message
        if "Connection refused" in message or "UNAVAILABLE" in message:
            pretty = (
                "Could not connect to the RS3 scripting server.\n\n"
                "Close RS3 if it is open without scripting, then Extract again.\n\n"
                + message
            )
        self.QtWidgets.QMessageBox.critical(self.window, "Extract failed", pretty)

    def _on_criterion_or_stage(self, *_args: Any) -> None:
        if self._updating_controls or self.dataset is None:
            return
        if self._worker is not None and self._worker.thread.isRunning():
            return
        # Criterion / stage need a fresh RS3 pull.
        self._log("Criterion or stage changed — re-extracting…")
        self._start_extract()

    def _on_mode_changed(self, *_args: Any) -> None:
        if self._updating_controls or self.dataset is None:
            return
        try:
            self.dataset.failure_mode = parse_failure_mode(
                self.mode_combo.currentText()
            )
        except ValueError:
            return
        try:
            self._render_dataset(float(self.limit_spin.value()))
        except Exception:  # noqa: BLE001
            self._log(traceback.format_exc())

    def _on_limit_spin(self, value: float) -> None:
        if self._updating_controls:
            return
        self._updating_controls = True
        try:
            self._sync_slider_from_limit(value)
        finally:
            self._updating_controls = False
        if self.dataset is not None:
            try:
                self._render_dataset(float(value), rebuild_mesh=False)
            except Exception:  # noqa: BLE001
                self._log(traceback.format_exc())

    def _on_limit_slider(self, pos: int) -> None:
        if self._updating_controls or self.dataset is None:
            return
        lo = self.limit_spin.minimum()
        hi = self.limit_spin.maximum()
        value = lo + (hi - lo) * (pos / 1000.0)
        self._updating_controls = True
        try:
            self.limit_spin.setValue(value)
        finally:
            self._updating_controls = False
        try:
            self._render_dataset(float(value), rebuild_mesh=False)
        except Exception:  # noqa: BLE001
            self._log(traceback.format_exc())

    def _sync_slider_from_limit(self, limit: float) -> None:
        lo = self.limit_spin.minimum()
        hi = self.limit_spin.maximum()
        if hi <= lo:
            self.limit_slider.setValue(0)
            return
        frac = (limit - lo) / (hi - lo)
        self.limit_slider.setValue(int(round(max(0.0, min(1.0, frac)) * 1000)))

    def _render_dataset(self, limit: float, *, rebuild_mesh: bool = True) -> None:
        if self.dataset is None or limit <= 0:
            return
        local_fos, failed = compute_local_fos_array(self.dataset, limit)
        mesh, scalar_type = build_fos_mesh(self.dataset, local_fos)
        clim = fos_clim(local_fos, self.dataset)

        try:
            if scalar_type == "cell":
                mesh.set_active_scalars("Local FoS", preference="cell")
            else:
                mesh.set_active_scalars("Local FoS", preference="point")
        except TypeError:
            mesh.set_active_scalars("Local FoS")

        if self._mesh_actor is not None:
            try:
                self.plotter.remove_actor(self._mesh_actor)
            except Exception:  # noqa: BLE001
                pass
            self._mesh_actor = None

        # Discrete-ish solid coloring (FLAC-like bands: red=low FoS).
        add_kwargs = dict(
            scalars="Local FoS",
            cmap="jet_r",
            n_colors=10,
            clim=clim,
            show_edges=False,
            lighting=True,
            smooth_shading=False,
            scalar_bar_args={
                "title": "Local FoS",
                "color": "black",
                "n_labels": 6,
                "fmt": "%.3g",
            },
        )
        try:
            self._mesh_actor = self.plotter.add_mesh(
                mesh, preference=scalar_type, **add_kwargs
            )
        except TypeError:
            self._mesh_actor = self.plotter.add_mesh(mesh, **add_kwargs)
        n_failed = int(failed.sum())
        self.status.showMessage(
            f"Limit={limit:.6g} | nodes={self.dataset.n_nodes} | "
            f"elements={self.dataset.n_elements} | failed={n_failed} | "
            f"min FoS={float(np.nanmin(local_fos)):.4g} | "
            f"{self.dataset.criterion.value} / {self.dataset.failure_mode.value}"
        )
        self.plotter.reset_camera()
        self.plotter.render()

    def run(self) -> int:
        self.window.show()
        return self.app.exec()


def launch_viewer(
    *,
    model: Path | None = None,
    port: int = 60064,
    stage: int = 1,
    criterion: str = "total_displacement",
    mode: str = "absolute",
    no_start: bool = False,
    auto_extract: bool = False,
) -> int:
    """Create and run the FoS main window."""
    win = FoSMainWindow(
        model=model,
        port=port,
        stage=stage,
        criterion=criterion,
        mode=mode,
        no_start=no_start,
        auto_extract=auto_extract,
    )
    return win.run()


# Back-compat for older call sites.
def show_contour_viewer(dataset: ContourDataset, *, initial_limit: float, **_kwargs) -> None:
    """Deprecated thin wrapper — opens the Qt viewer with cached data only."""
    QtCore, QtWidgets, _, _ = _require_qt_pyvista()
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    win = FoSMainWindow(auto_extract=False)
    win.dataset = dataset
    win._updating_controls = True
    try:
        lo, hi = default_limit_range(dataset, initial_limit)
        win.limit_spin.setRange(lo, hi)
        win.limit_spin.setValue(initial_limit)
        win._sync_slider_from_limit(initial_limit)
        win.model_edit.setText(dataset.model_path)
        win.stage_spin.setValue(dataset.stage_number)
        win.criterion_combo.setCurrentText(dataset.criterion.value)
        win.mode_combo.setCurrentText(dataset.failure_mode.value)
    finally:
        win._updating_controls = False
    win._render_dataset(initial_limit)
    win.window.show()
    app.exec()
