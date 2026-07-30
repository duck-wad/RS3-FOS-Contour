"""
Dash + Plotly web UI for RS3 local FoS contours.

Same stack as RS3 Compute Analyzer: browser WebGL via Plotly Mesh3d.
"""

from __future__ import annotations

import os
import tempfile
import time
import traceback
import webbrowser
from pathlib import Path
from threading import Thread, Timer
from typing import Optional

import numpy as np
from dash import (
    Dash,
    Input,
    Output,
    Patch,
    State,
    callback,
    clientside_callback,
    dcc,
    html,
    no_update,
)

from .criteria import Criterion, FailureMode, parse_criterion
from .dataset import ContourDataset, compute_local_fos_array, histories_to_dataset
from .export import suggest_limit
from .slice_plane import (
    AXIS_LABEL,
    cut_mesh_with_plane,
    section_slider_range,
)
from .web_mesh import (
    intensities_for_limit,
    intensities_for_slice,
    make_fos_figure,
    prepare_surface_cache,
)

# Shared extract cache (single-user local app).
_dataset: Optional[ContourDataset] = None
_datasets: dict[str, ContourDataset] = {}
_suggestions: Optional[dict[str, float]] = None
_suggestions_by: dict[str, dict[str, float]] = {}
_active_criterion: str = "total_displacement"
_log_lines: list[str] = []
_no_start: bool = False
_extract_running: bool = False
_extract_started_at: float = 0.0
_extract_job_id: int = 0
_extract_finished_job: int = 0
_extract_applied_job: int = 0
_extract_error: Optional[str] = None
_extract_initial_limit: Optional[float] = None
_pending_figure = None
_pending_status: Optional[str] = None
_pending_slider: Optional[tuple[float, float, float, float, dict, str]] = None
_slice_cache = None
_view_mode: str = "solid"
_section_plane: str = "XY"
_section_position: Optional[float] = None

_VIEWER_CRITERIA = (
    Criterion.TOTAL_DISPLACEMENT,
    Criterion.MAX_SHEAR_STRAIN,
)

_TEMP_FILE_PATH = os.path.join(tempfile.gettempdir(), "fos_contour_selected_model.txt")
_DEFAULT_HTTP_PORT = 8051
_FAILURE_MODE = FailureMode.ABSOLUTE


def _append_log(msg: str) -> None:
    """Log with an elapsed-time stamp so slow steps visibly progress."""
    if _extract_running and _extract_started_at:
        elapsed = time.monotonic() - _extract_started_at
        stamp = f"[{int(elapsed) // 60:d}:{int(elapsed) % 60:02d}] "
    else:
        stamp = time.strftime("[%H:%M:%S] ")
    for line in str(msg).splitlines() or [""]:
        _log_lines.append(f"{stamp}{line}")
    if len(_log_lines) > 400:
        del _log_lines[:-400]


def _log_text() -> str:
    return "\n".join(_log_lines[-80:])


def _last_log_line() -> str:
    return _log_lines[-1] if _log_lines else ""


def _start_extract_thread(
    model_path: str,
    port: int,
    criterion: str,
) -> bool:
    """
    Kick off extraction on a background thread.

    Returns False if an extract is already running. The Dash request returns
    immediately so Interval polling can stream the log while RS3 works.
    """
    global _dataset, _suggestions, _extract_running, _extract_started_at
    global _extract_job_id, _extract_error, _extract_initial_limit
    global _datasets, _suggestions_by, _active_criterion
    global _pending_figure, _pending_status, _pending_slider
    global _slice_cache, _view_mode, _section_plane, _section_position

    if _extract_running:
        _append_log("Extract already in progress — ignoring duplicate click.")
        return False

    _log_lines.clear()
    _dataset = None
    _datasets = {}
    _suggestions = None
    _suggestions_by = {}
    _extract_error = None
    _extract_initial_limit = None
    _pending_figure = None
    _pending_status = None
    _pending_slider = None
    _slice_cache = None
    _view_mode = "solid"
    _section_plane = "XY"
    _section_position = None
    _extract_job_id += 1
    job_id = _extract_job_id
    _extract_started_at = time.monotonic()
    _extract_running = True
    _append_log("Starting new extraction…")

    def worker() -> None:
        global _dataset, _suggestions, _extract_running
        global _extract_finished_job, _extract_error, _extract_initial_limit
        global _datasets, _suggestions_by, _active_criterion
        global _pending_figure, _pending_status, _pending_slider
        try:
            if not model_path or not Path(model_path).exists():
                raise FileNotFoundError(f"Model not found: {model_path}")
            datasets, suggestions_by, active, initial_limit = _extract_datasets(
                model_path,
                port,
                criterion or "total_displacement",
                no_start=_no_start,
            )
            # Ignore stale jobs if the user clicked Extract again.
            if job_id != _extract_job_id:
                return
            _datasets = datasets
            _suggestions_by = suggestions_by
            _active_criterion = active
            _dataset = datasets[active]
            _suggestions = suggestions_by[active]
            _extract_initial_limit = float(initial_limit)
            _extract_error = None

            # Build the Plotly figure here (not in the Dash callback) so the
            # UI keeps streaming logs and a large open-pit mesh cannot freeze
            # the server mid-request.
            _append_log("Building Plotly figure…")
            t_fig = time.monotonic()
            limit = _nice_limit(float(initial_limit))
            _append_log("  computing local FoS…")
            lo, hi = _limit_bounds(_dataset, limit)
            _append_log(
                f"  assembling Mesh3d "
                f"({_dataset.n_surface_nodes:,} verts / "
                f"{_dataset.n_exterior_tris:,} tris)…"
            )
            fig, status = _figure_for_limit(_dataset, limit)
            marks = _limit_marks(lo, hi, limit)
            readout = f"Limit = {_fmt_limit(limit)} (suggested)"
            _pending_figure = fig
            _pending_status = status
            _pending_slider = (lo, hi, limit, _limit_step(lo, hi), marks, readout)
            _append_log(
                f"Figure ready in {time.monotonic() - t_fig:.1f}s — "
                f"{_dataset.n_surface_nodes:,} surface verts, "
                f"{_dataset.n_exterior_tris:,} tris "
                f"(volume nodes={_dataset.n_nodes:,})."
            )
        except Exception as exc:  # noqa: BLE001
            if job_id != _extract_job_id:
                return
            msg = str(exc).strip() or exc.__class__.__name__
            _append_log(msg)
            if "No computed results" not in msg and "No SRF" not in msg:
                _append_log(traceback.format_exc())
            _extract_error = msg
            _dataset = None
            _datasets = {}
            _suggestions = None
            _suggestions_by = {}
            _extract_initial_limit = None
            _pending_figure = None
            _pending_status = None
            _pending_slider = None
        finally:
            if job_id == _extract_job_id:
                _extract_running = False
                _extract_finished_job = job_id

    Thread(target=worker, daemon=True, name=f"fos-extract-{job_id}").start()
    return True


def _apply_finished_extract(token: int):
    """Push the pre-built figure into the UI once a background extract finishes."""
    global _extract_applied_job, _pending_figure, _pending_status, _pending_slider
    global _section_position, _view_mode, _section_plane, _slice_cache
    job = _extract_finished_job
    if job <= _extract_applied_job:
        return None
    _extract_applied_job = job

    # Outputs after the shared limit-slider fields:
    # section_min, section_max, section_value, section_step, section_marks,
    # section_readout, section_controls_disabled, view_mode, plane
    if _extract_error or _dataset is None or _pending_figure is None:
        return (
            no_update,
            "Extract failed — see log.",
            _log_text(),
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            token,
            True,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            True,
            "solid",
            "XY",
        )

    lo, hi, limit, step, marks, readout = _pending_slider or (
        0.0,
        1.0,
        0.5,
        0.01,
        None,
        "Limit = ?",
    )
    fig = _pending_figure
    status = _pending_status or "Extract complete."
    _pending_figure = None
    _pending_status = None
    _pending_slider = None
    _view_mode = "solid"
    _section_plane = "XY"
    _slice_cache = None
    s_lo, s_hi, s_mid = section_slider_range(_dataset, "XY")
    _section_position = s_mid
    s_step = _section_step(s_lo, s_hi)
    s_marks = _section_marks(s_lo, s_hi, s_mid)
    s_readout = _section_readout("XY", s_mid)
    return (
        fig,
        status,
        _log_text(),
        lo,
        hi,
        limit,
        step,
        marks,
        readout,
        (token or 0) + 1,
        True,
        s_lo,
        s_hi,
        s_mid,
        s_step,
        s_marks,
        s_readout,
        True,  # section controls disabled in solid mode
        "solid",
        "XY",
    )


def _section_step(lo: float, hi: float) -> float:
    span = max(float(hi) - float(lo), 1e-9)
    step = span / 200.0
    # Keep a readable step size.
    if step <= 0:
        return 1.0
    mag = 10 ** np.floor(np.log10(step))
    return float(max(mag, step))


def _section_marks(lo: float, hi: float, value: float) -> dict:
    return {
        float(lo): f"{lo:.4g}",
        float(value): f"{value:.4g}",
        float(hi): f"{hi:.4g}",
    }


def _section_readout(plane: str, position: float) -> str:
    from .slice_plane import plane_axis

    axis = AXIS_LABEL[plane_axis(plane)]
    return f"{plane} plane · {axis} = {float(position):.4g}"


def _btn(color: str) -> dict:
    return {
        "padding": "8px 12px",
        "background": color,
        "color": "white",
        "border": "none",
        "borderRadius": "5px",
        "cursor": "pointer",
        "flex": "1",
    }


def _input() -> dict:
    return {"width": "100%", "padding": "6px", "boxSizing": "border-box"}


def _labeled(label: str, child) -> html.Div:
    return html.Div(
        [
            html.Label(label, style={"fontWeight": "bold", "display": "block"}),
            child,
        ],
        style={"marginBottom": "8px", "flex": "1"},
    )


def _empty_figure():
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.update_layout(
        title="No data yet",
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="white",
        uirevision="fos-contour",
        scene=dict(aspectmode="data", bgcolor="white", uirevision="fos-contour"),
    )
    return fig


def _fmt_limit(value: float) -> str:
    """Compact limit label (avoids long float tails on the slider)."""
    return f"{_nice_limit(value):.4g}"


def _nice_limit(value: float) -> float:
    """Round a limit to 4 significant digits as a real float (for the slider)."""
    v = float(value)
    if v == 0.0:
        return 0.0
    return float(f"{v:.4g}")


def _limit_step(lo: float, hi: float) -> float:
    """Coarse slider step so tooltips stay readable."""
    span = max(float(hi) - float(lo), 1e-30)
    rough = span / 100.0
    exp = int(np.floor(np.log10(rough)))
    return float(10.0**exp)


def _limit_marks(lo: float, hi: float, value: float) -> dict:
    return {
        lo: _fmt_limit(lo),
        value: _fmt_limit(value),
        hi: _fmt_limit(hi),
    }


def _limit_bounds(dataset: ContourDataset, initial_limit: float) -> tuple[float, float]:
    finite = dataset.values[np.isfinite(dataset.values)]
    initial = _nice_limit(initial_limit)
    if finite.size == 0:
        lo, hi = initial * 0.2, initial * 2.0
    else:
        # Avoid pathological lows like 1e-16 that blow up slider precision.
        p1 = float(np.percentile(finite, 1))
        p99 = float(np.percentile(finite, 99))
        lo = max(p1, initial * 0.05, 1e-12)
        hi = max(p99, initial * 2.0, lo * 10.0)
    lo = min(lo, initial * 0.2)
    hi = max(hi, initial * 2.0)
    if hi <= lo:
        hi = lo * 10.0
    return _nice_limit(lo), _nice_limit(hi)


def _status_for_limit(dataset: ContourDataset, limit: float, local_fos: np.ndarray, failed: np.ndarray) -> str:
    base = (
        f"Limit={_fmt_limit(limit)} | nodes={dataset.n_nodes} | "
        f"elements={dataset.n_elements} | failed={int(failed.sum())} | "
        f"min FoS={float(np.nanmin(local_fos)):.4g} | "
        f"{dataset.criterion.value} / {dataset.failure_mode.value} | "
        f"stage={dataset.stage_number}"
    )
    if _view_mode == "section" and _slice_cache is not None:
        base += (
            f" | section {_slice_cache.plane} "
            f"({AXIS_LABEL[_slice_cache.axis]}={_slice_cache.position:.4g}, "
            f"tris={_slice_cache.n_tris:,})"
        )
    return base


def _ensure_slice_cache(dataset: ContourDataset, plane: str, position: float):
    """Rebuild the cut mesh when plane/position change."""
    global _slice_cache
    from .slice_plane import plane_axis, prepare_element_accel

    plane_u = str(plane).upper()
    pos = float(position)
    if (
        _slice_cache is not None
        and _slice_cache.plane == plane_u
        and abs(_slice_cache.position - pos) <= 1e-9
    ):
        return _slice_cache

    # Build / reuse the element AABB index only when sectioning is requested.
    ds_map = _datasets if _datasets else {dataset.criterion.value: dataset}
    prepare_element_accel(ds_map, progress_callback=_append_log)

    t0 = time.monotonic()
    axis = plane_axis(plane_u)
    _append_log(
        f"Cutting section {plane_u} @ {AXIS_LABEL[axis]}={pos:.4g}…"
    )
    _slice_cache = cut_mesh_with_plane(dataset, plane=plane_u, position=pos)
    _append_log(
        f"Section {plane_u} @ {AXIS_LABEL[_slice_cache.axis]}={pos:.4g}: "
        f"{_slice_cache.n_tris:,} tris in {time.monotonic() - t0:.2f}s."
    )
    return _slice_cache


def _figure_for_limit(
    dataset: ContourDataset,
    limit: float,
    *,
    camera: dict | None = None,
    view_mode: str | None = None,
    plane: str | None = None,
    position: float | None = None,
):
    global _view_mode, _section_plane, _section_position
    mode = (view_mode or _view_mode or "solid").lower()
    if mode in ("cross-section", "cross_section"):
        mode = "section"
    pln = (plane or _section_plane or "XY").upper()
    if position is None:
        position = _section_position
    if position is None and mode == "section":
        _lo, _hi, position = section_slider_range(dataset, pln)

    _view_mode = mode
    _section_plane = pln
    if position is not None:
        _section_position = float(position)

    local_fos, failed = compute_local_fos_array(dataset, limit)
    slice_cache = None
    if mode == "section":
        slice_cache = _ensure_slice_cache(dataset, pln, float(position))
    fig = make_fos_figure(
        dataset,
        local_fos,
        failed=failed,
        title=Path(dataset.model_path).name or "Local FoS",
        camera=camera,
        view_mode=mode,
        plane=pln,
        position=_section_position,
        slice_cache=slice_cache,
    )
    return fig, _status_for_limit(dataset, limit, local_fos, failed)


def _patch_for_limit(
    dataset: ContourDataset,
    limit: float,
    *,
    camera: dict | None = None,
):
    """Update FoS colors only — keeps the current camera (no full figure replace)."""
    local_fos, failed = compute_local_fos_array(dataset, limit)
    patched = Patch()
    if _view_mode == "section" and _slice_cache is not None and _slice_cache.blends:
        intensities, clim, raw_fos = intensities_for_slice(
            dataset, local_fos, _slice_cache, failed=failed
        )
        patched["data"][0]["intensity"] = intensities
        patched["data"][0]["customdata"] = raw_fos
        patched["data"][0]["cmin"] = clim[0]
        patched["data"][0]["cmax"] = clim[1]
    else:
        intensities, clim, raw_fos = intensities_for_limit(
            dataset, local_fos, failed=failed
        )
        patched["data"][0]["intensity"] = intensities
        if dataset.exterior_i:
            patched["data"][0]["customdata"] = raw_fos
        patched["data"][0]["cmin"] = clim[0]
        patched["data"][0]["cmax"] = clim[1]
    if camera:
        patched["layout"]["scene"]["camera"] = camera
    return patched, _status_for_limit(dataset, limit, local_fos, failed)


def create_layout(
    *,
    initial_model: str = "",
    criterion: str = "total_displacement",
    port: int = 60064,
    initial_figure=None,
    limit_min: float = 0.0,
    limit_max: float = 1.0,
    limit_value: float = 0.5,
    status: str = "Load a computed .rs3v3 and click Extract.",
    extract_token: int = 0,
) -> html.Div:
    marks = None
    if limit_max > limit_min:
        marks = _limit_marks(limit_min, limit_max, limit_value)
    return html.Div(
        [
            dcc.Interval(id="file-poll", interval=400, n_intervals=0, disabled=True),
            dcc.Interval(id="log-poll", interval=600, n_intervals=0, disabled=True),
            dcc.Store(id="extract-token", data=extract_token),
            dcc.Store(id="camera-store", data=None),
            html.Div(
                [
                    html.Div(
                        [
                            html.H3(
                                "RS3 Local FoS Contours",
                                style={"margin": "0 0 12px 0", "fontSize": "18px"},
                            ),
                            html.Label("Model (.rs3v3)", style={"fontWeight": "bold"}),
                            dcc.Input(
                                id="model-path",
                                type="text",
                                value=initial_model,
                                placeholder="Paste path or Browse…",
                                style={
                                    "width": "100%",
                                    "padding": "8px",
                                    "boxSizing": "border-box",
                                    "marginBottom": "6px",
                                },
                                debounce=True,
                            ),
                            html.Div(
                                [
                                    html.Button(
                                        "Browse",
                                        id="browse-btn",
                                        n_clicks=0,
                                        style=_btn("#e85a1c"),
                                    ),
                                    html.Button(
                                        "Extract from RS3",
                                        id="extract-btn",
                                        n_clicks=0,
                                        style=_btn("#2b6cb0"),
                                    ),
                                ],
                                style={
                                    "display": "flex",
                                    "gap": "6px",
                                    "marginBottom": "12px",
                                },
                            ),
                            _labeled(
                                "Port",
                                dcc.Input(
                                    id="port-input",
                                    type="text",
                                    value=str(port),
                                    style=_input(),
                                    debounce=True,
                                ),
                            ),
                            _labeled(
                                "Criterion",
                                dcc.Dropdown(
                                    id="criterion-dropdown",
                                    options=[
                                        {
                                            "label": "total_displacement",
                                            "value": "total_displacement",
                                        },
                                        {
                                            "label": "max_shear_strain",
                                            "value": "max_shear_strain",
                                        },
                                    ],
                                    value=criterion,
                                    clearable=False,
                                    searchable=False,
                                ),
                            ),
                            html.Label(
                                "Limit",
                                style={"fontWeight": "bold", "marginTop": "4px"},
                            ),
                            dcc.Slider(
                                id="limit-slider",
                                min=limit_min,
                                max=limit_max,
                                step=_limit_step(limit_min, limit_max)
                                if limit_max > limit_min
                                else 0.001,
                                value=_nice_limit(limit_value),
                                marks=marks,
                                # Hide the float-noisy tooltip / direct input;
                                # the readout below is formatted to 4 sig digits.
                                tooltip=None,
                                allow_direct_input=False,
                                updatemode="mouseup",
                            ),
                            html.Div(
                                id="limit-readout",
                                children=f"Limit = {_fmt_limit(limit_value)}",
                                style={"fontSize": "13px", "margin": "4px 0 10px"},
                            ),
                            _labeled(
                                "View",
                                dcc.Dropdown(
                                    id="view-mode",
                                    options=[
                                        {
                                            "label": "Solid surface",
                                            "value": "solid",
                                        },
                                        {
                                            "label": "Cross-section",
                                            "value": "section",
                                        },
                                    ],
                                    value="solid",
                                    clearable=False,
                                    searchable=False,
                                ),
                            ),
                            _labeled(
                                "Section plane",
                                dcc.Dropdown(
                                    id="section-plane",
                                    options=[
                                        {
                                            "label": "XY (cut along Z)",
                                            "value": "XY",
                                        },
                                        {
                                            "label": "XZ (cut along Y)",
                                            "value": "XZ",
                                        },
                                        {
                                            "label": "YZ (cut along X)",
                                            "value": "YZ",
                                        },
                                    ],
                                    value="XY",
                                    clearable=False,
                                    searchable=False,
                                    disabled=True,
                                ),
                            ),
                            html.Label(
                                "Section position",
                                style={"fontWeight": "bold", "marginTop": "4px"},
                            ),
                            dcc.Slider(
                                id="section-slider",
                                min=0.0,
                                max=1.0,
                                step=0.01,
                                value=0.5,
                                marks=None,
                                tooltip=None,
                                allow_direct_input=False,
                                updatemode="mouseup",
                                disabled=True,
                            ),
                            html.Div(
                                id="section-readout",
                                children="XY plane · Z = —",
                                style={
                                    "fontSize": "13px",
                                    "margin": "4px 0 10px",
                                    "color": "#666",
                                },
                            ),
                            html.Div(
                                id="status-bar",
                                children=status,
                                style={
                                    "fontSize": "12px",
                                    "color": "#333",
                                    "background": "#f0f4f8",
                                    "padding": "8px",
                                    "borderRadius": "4px",
                                    "marginBottom": "8px",
                                    "minHeight": "40px",
                                },
                            ),
                            html.Label("Log", style={"fontWeight": "bold"}),
                            html.Pre(
                                id="log-panel",
                                children=_log_text(),
                                style={
                                    "fontSize": "11px",
                                    "background": "#1a202c",
                                    "color": "#e2e8f0",
                                    "padding": "8px",
                                    "borderRadius": "4px",
                                    "height": "180px",
                                    "overflow": "auto",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                        ],
                        style={
                            "width": "340px",
                            "minWidth": "300px",
                            "padding": "12px",
                            "boxSizing": "border-box",
                            "borderRight": "1px solid #ddd",
                            "overflowY": "auto",
                            "height": "100vh",
                            "background": "#fafafa",
                        },
                    ),
                    html.Div(
                        [
                            dcc.Graph(
                                id="fos-graph",
                                figure=initial_figure or _empty_figure(),
                                style={"height": "100vh"},
                                config={
                                    "scrollZoom": True,
                                    "displaylogo": False,
                                },
                            )
                        ],
                        style={"flex": "1", "height": "100vh"},
                    ),
                ],
                style={"display": "flex", "height": "100vh", "overflow": "hidden"},
            ),
        ]
    )


def _run_file_dialog() -> None:
    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        root.focus_force()
        path = filedialog.askopenfilename(
            title="Select RS3 model",
            filetypes=[("RS3 model", "*.rs3v3"), ("All files", "*.*")],
        )
        root.destroy()
        if path:
            with open(_TEMP_FILE_PATH, "w", encoding="utf-8") as f:
                f.write(path)
    except Exception as exc:  # noqa: BLE001
        _append_log(f"File dialog error: {exc}")


def _resolve_final_stage(model) -> int:
    """SSR FoS maps use the final analysis stage only."""
    try:
        stage = int(model.getActiveStage())
        if stage >= 1:
            return stage
    except Exception:  # noqa: BLE001
        pass
    return 1


def _extract_datasets(
    model_path: str,
    port: int,
    preferred_criterion: str,
    *,
    no_start: bool = False,
) -> tuple[dict[str, ContourDataset], dict[str, dict[str, float]], str, float]:
    """Pull displacement + shear strain in one RS3 pass; return both caches."""
    from .rs3_extract import extract_nodal_histories
    from .session import connect_model

    preferred = parse_criterion(preferred_criterion)
    failure_mode = _FAILURE_MODE
    model = Path(model_path)

    def progress(msg: str) -> None:
        _append_log(msg)

    progress(f"Model: {model.name}")
    progress(
        "Pulling total_displacement + max_shear_strain together "
        f"(RS3 port {port})…"
    )
    progress("Step 1/5: connecting to RS3 (may take a while if RS3 is busy)…")
    t0 = time.monotonic()
    session = connect_model(
        model,
        port=port,
        force_no_start=no_start,
        progress_callback=progress,
    )
    progress(f"Connected in {time.monotonic() - t0:.1f}s.")
    try:
        stage = _resolve_final_stage(session.model)
        progress(f"Step 2/5: using final stage {stage}.")
        progress("Step 3/5: reading SRF trials from RS3 (both criteria)…")
        t1 = time.monotonic()
        trials, histories_by, elements = extract_nodal_histories(
            session.model,
            criteria=list(_VIEWER_CRITERIA),
            stage_number=stage,
            surface_only=False,
            include_elements=True,
            progress_callback=progress,
        )
        n_nodes = len(next(iter(histories_by.values()))) if histories_by else 0
        progress(
            f"Read {len(trials)} SRF trials in {time.monotonic() - t1:.1f}s "
            f"({n_nodes} nodes × {len(histories_by)} criteria)."
        )
        progress("Step 4/5: suggesting limits for each criterion…")
        datasets: dict[str, ContourDataset] = {}
        suggestions_by: dict[str, dict[str, float]] = {}
        # One shared connectivity list — both criteria reuse the same mesh.
        elements_shared = elements if elements is not None else []
        for crit, histories in histories_by.items():
            suggestions = suggest_limit(
                trials, histories, failure_mode=failure_mode
            )
            suggestions_by[crit.value] = suggestions
            progress(f"  [{crit.value}] suggested={suggestions['suggested']:g}")
            progress(f"  [{crit.value}] packing {len(histories):,} nodal histories…")
            t_pack = time.monotonic()
            datasets[crit.value] = histories_to_dataset(
                trials,
                histories,
                criterion=crit,
                failure_mode=failure_mode,
                stage_number=stage,
                model_path=str(model),
                elements=elements_shared,
            )
            progress(
                f"  [{crit.value}] packed in {time.monotonic() - t_pack:.1f}s."
            )

        progress("Step 5/5: building exterior surface cache…")
        prepare_surface_cache(datasets, progress_callback=progress)
        # Cross-section element index is built lazily on first section view so
        # solid FoS display is not blocked on large open-pit meshes.
        progress("Contour caches ready.")
        active = preferred.value if preferred.value in datasets else next(iter(datasets))
        initial_limit = float(suggestions_by[active]["suggested"])
        sample = datasets[active]
        progress(
            f"Extract complete in {time.monotonic() - t0:.1f}s — "
            f"{sample.n_nodes} nodes, {sample.n_elements} elements, "
            f"{sample.n_exterior_tris} exterior tris. "
            "Criterion switches are local (no RS3 re-pull)."
        )
        return datasets, suggestions_by, active, initial_limit
    finally:
        try:
            session.close(keep_open=True)
        except Exception as exc:  # noqa: BLE001
            progress(f"Warning during session cleanup: {exc}")


def _activate_criterion(criterion_name: str) -> tuple[ContourDataset, dict[str, float], float]:
    """Switch the active cached criterion without talking to RS3."""
    global _dataset, _suggestions, _active_criterion, _extract_initial_limit
    key = parse_criterion(criterion_name).value
    if key not in _datasets:
        raise KeyError(f"No cached extract for criterion '{key}'. Click Extract first.")
    _active_criterion = key
    _dataset = _datasets[key]
    _suggestions = _suggestions_by[key]
    initial_limit = _nice_limit(float(_suggestions["suggested"]))
    _extract_initial_limit = initial_limit
    return _dataset, _suggestions, initial_limit


def _apply_criterion_switch(criterion_name: str, token: int, camera=None):
    """Build UI outputs after a local criterion switch."""
    dataset, _suggestions_local, initial_limit = _activate_criterion(criterion_name)
    lo, hi = _limit_bounds(dataset, initial_limit)
    fig, status = _figure_for_limit(dataset, initial_limit, camera=camera)
    marks = _limit_marks(lo, hi, initial_limit)
    readout = f"Limit = {_fmt_limit(initial_limit)} (suggested)"
    _append_log(
        f"Switched to {dataset.criterion.value} (cached) — "
        f"suggested limit {_fmt_limit(initial_limit)}."
    )
    return (
        fig,
        status,
        _log_text(),
        lo,
        hi,
        initial_limit,
        _limit_step(lo, hi),
        marks,
        readout,
        token,
    )


def create_app(
    *,
    initial_model: str = "",
    criterion: str = "total_displacement",
    port: int = 60064,
    no_start: bool = False,
    initial_figure=None,
    limit_min: float = 0.0,
    limit_max: float = 1.0,
    limit_value: float = 0.5,
    status: str = "Load a computed .rs3v3 and click Extract.",
    extract_token: int = 0,
) -> Dash:
    global _no_start
    _no_start = no_start

    app = Dash(__name__, suppress_callback_exceptions=True)
    app.title = "RS3 Local FoS Contours"
    app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            html, body { margin: 0; padding: 0; overflow: hidden; height: 100%;
                         font-family: Segoe UI, Arial, sans-serif; }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""
    app.layout = create_layout(
        initial_model=initial_model,
        criterion=criterion,
        port=port,
        initial_figure=initial_figure,
        limit_min=limit_min,
        limit_max=limit_max,
        limit_value=limit_value,
        status=status,
        extract_token=extract_token,
    )

    @callback(
        Output("file-poll", "disabled"),
        Output("file-poll", "n_intervals"),
        Input("browse-btn", "n_clicks"),
        prevent_initial_call=True,
    )
    def start_browse(_n_clicks):
        if os.path.exists(_TEMP_FILE_PATH):
            try:
                os.remove(_TEMP_FILE_PATH)
            except OSError:
                pass
        Thread(target=_run_file_dialog, daemon=True).start()
        return False, 0

    @callback(
        Output("model-path", "value"),
        Output("file-poll", "disabled", allow_duplicate=True),
        Input("file-poll", "n_intervals"),
        prevent_initial_call=True,
    )
    def poll_browse(n_intervals):
        # Stop polling if the dialog was cancelled (no file written).
        if not os.path.exists(_TEMP_FILE_PATH):
            if (n_intervals or 0) >= 75:  # ~30s at 400ms
                return no_update, True
            return no_update, no_update
        try:
            with open(_TEMP_FILE_PATH, "r", encoding="utf-8") as f:
                path = f.read().strip()
            os.remove(_TEMP_FILE_PATH)
        except OSError:
            return no_update, True
        if not path:
            return no_update, True
        return path, True

    @callback(
        Output("status-bar", "children", allow_duplicate=True),
        Output("log-panel", "children", allow_duplicate=True),
        Output("log-poll", "disabled", allow_duplicate=True),
        Output("log-poll", "n_intervals", allow_duplicate=True),
        Input("extract-btn", "n_clicks"),
        State("model-path", "value"),
        State("port-input", "value"),
        State("criterion-dropdown", "value"),
        prevent_initial_call=True,
    )
    def on_extract(_n_clicks, model_path, port, criterion):
        """Start extract in a background thread; do not block the Dash server."""
        try:
            port_i = int(port or 60064)
        except (TypeError, ValueError):
            port_i = 60064
        started = _start_extract_thread(
            str(model_path or ""),
            port_i,
            criterion or "total_displacement",
        )
        if not started:
            return (
                f"Busy — {_last_log_line()}",
                _log_text(),
                False,
                no_update,
            )
        return (
            "Extracting… (log updates live)",
            _log_text(),
            False,
            0,
        )

    @callback(
        Output("fos-graph", "figure", allow_duplicate=True),
        Output("status-bar", "children", allow_duplicate=True),
        Output("limit-readout", "children", allow_duplicate=True),
        Output("log-panel", "children", allow_duplicate=True),
        Input("limit-slider", "value"),
        State("extract-token", "data"),
        State("camera-store", "data"),
        prevent_initial_call=True,
    )
    def on_limit(limit, token, camera):
        global _dataset
        if _dataset is None or not token or _extract_running:
            return no_update, no_update, no_update, no_update
        cam = camera if isinstance(camera, dict) else None
        try:
            limit_f = _nice_limit(float(limit))
            if limit_f <= 0:
                return no_update, no_update, no_update, no_update
            patched, status = _patch_for_limit(_dataset, limit_f, camera=cam)
            return patched, status, f"Limit = {_fmt_limit(limit_f)}", _log_text()
        except Exception:  # noqa: BLE001
            _append_log(traceback.format_exc())
            try:
                limit_f = _nice_limit(float(limit))
                fig, status = _figure_for_limit(_dataset, limit_f, camera=cam)
                return fig, status, f"Limit = {_fmt_limit(limit_f)}", _log_text()
            except Exception:  # noqa: BLE001
                _append_log(traceback.format_exc())
                return no_update, "Update failed — see log.", no_update, _log_text()

    @callback(
        Output("fos-graph", "figure", allow_duplicate=True),
        Output("status-bar", "children", allow_duplicate=True),
        Output("log-panel", "children", allow_duplicate=True),
        Output("limit-slider", "min", allow_duplicate=True),
        Output("limit-slider", "max", allow_duplicate=True),
        Output("limit-slider", "value", allow_duplicate=True),
        Output("limit-slider", "step", allow_duplicate=True),
        Output("limit-slider", "marks", allow_duplicate=True),
        Output("limit-readout", "children", allow_duplicate=True),
        Output("extract-token", "data", allow_duplicate=True),
        Input("criterion-dropdown", "value"),
        State("extract-token", "data"),
        State("camera-store", "data"),
        prevent_initial_call=True,
    )
    def on_criterion_changed(criterion, token, camera):
        """Switch criterion from cache — no RS3 re-pull."""
        if not token or _extract_running or not _datasets:
            return (no_update,) * 10
        key = parse_criterion(criterion or "total_displacement").value
        if key == _active_criterion and key in _datasets:
            return (no_update,) * 10
        if key not in _datasets:
            _append_log(
                f"Criterion '{key}' not in cache — click Extract to pull both fields."
            )
            return (
                no_update,
                no_update,
                _log_text(),
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
            )
        cam = camera if isinstance(camera, dict) else None
        try:
            return _apply_criterion_switch(key, int(token or 0), camera=cam)
        except Exception:  # noqa: BLE001
            _append_log(traceback.format_exc())
            return (
                no_update,
                "Criterion switch failed — see log.",
                _log_text(),
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
            )

    @callback(
        Output("fos-graph", "figure"),
        Output("status-bar", "children"),
        Output("log-panel", "children"),
        Output("limit-slider", "min"),
        Output("limit-slider", "max"),
        Output("limit-slider", "value"),
        Output("limit-slider", "step"),
        Output("limit-slider", "marks"),
        Output("limit-readout", "children"),
        Output("extract-token", "data"),
        Output("log-poll", "disabled"),
        Output("section-slider", "min"),
        Output("section-slider", "max"),
        Output("section-slider", "value"),
        Output("section-slider", "step"),
        Output("section-slider", "marks"),
        Output("section-readout", "children"),
        Output("section-plane", "disabled"),
        Output("section-slider", "disabled"),
        Output("view-mode", "value"),
        Output("section-plane", "value"),
        Input("log-poll", "n_intervals"),
        State("extract-token", "data"),
        prevent_initial_call=True,
    )
    def stream_log(_n_intervals, token):
        """Live log while extract runs, then apply the finished mesh."""
        idle_tail = (no_update,) * 10  # section + view fields
        if _extract_running:
            elapsed = time.monotonic() - _extract_started_at
            status = f"Extracting… {elapsed:.0f}s — {_last_log_line()}"
            return (
                no_update,
                status,
                _log_text(),
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                False,
            ) + idle_tail

        applied = _apply_finished_extract(token or 0)
        if applied is not None:
            # Expand single disabled flag into plane + slider disabled.
            (
                fig,
                status,
                log,
                lo,
                hi,
                limit,
                step,
                marks,
                readout,
                tok,
                poll_off,
                s_lo,
                s_hi,
                s_mid,
                s_step,
                s_marks,
                s_readout,
                section_disabled,
                view_mode,
                plane,
            ) = applied
            return (
                fig,
                status,
                log,
                lo,
                hi,
                limit,
                step,
                marks,
                readout,
                tok,
                poll_off,
                s_lo,
                s_hi,
                s_mid,
                s_step,
                s_marks,
                s_readout,
                section_disabled,
                section_disabled,
                view_mode,
                plane,
            )

        return (
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            True,
        ) + idle_tail

    @callback(
        Output("fos-graph", "figure", allow_duplicate=True),
        Output("status-bar", "children", allow_duplicate=True),
        Output("log-panel", "children", allow_duplicate=True),
        Output("section-slider", "min", allow_duplicate=True),
        Output("section-slider", "max", allow_duplicate=True),
        Output("section-slider", "value", allow_duplicate=True),
        Output("section-slider", "step", allow_duplicate=True),
        Output("section-slider", "marks", allow_duplicate=True),
        Output("section-readout", "children", allow_duplicate=True),
        Output("section-plane", "disabled", allow_duplicate=True),
        Output("section-slider", "disabled", allow_duplicate=True),
        Input("view-mode", "value"),
        Input("section-plane", "value"),
        Input("section-slider", "value"),
        State("limit-slider", "value"),
        State("extract-token", "data"),
        State("camera-store", "data"),
        prevent_initial_call=True,
    )
    def on_section_changed(view_mode, plane, position, limit, token, camera):
        """Switch solid/section view or move the cutting plane."""
        global _view_mode, _section_plane, _section_position, _slice_cache
        if _dataset is None or not token or _extract_running:
            return (no_update,) * 11

        mode = (view_mode or "solid").lower()
        if mode in ("cross-section", "cross_section"):
            mode = "section"
        pln = (plane or "XY").upper()
        cam = camera if isinstance(camera, dict) else None

        try:
            limit_f = _nice_limit(float(limit)) if limit is not None else None
            if limit_f is None or limit_f <= 0:
                if _extract_initial_limit is not None:
                    limit_f = _nice_limit(float(_extract_initial_limit))
                else:
                    return (no_update,) * 11

            if mode != "section":
                _view_mode = "solid"
                _slice_cache = None
                fig, status = _figure_for_limit(
                    _dataset,
                    limit_f,
                    camera=cam,
                    view_mode="solid",
                )
                # Keep current section slider range; just disable controls.
                return (
                    fig,
                    status,
                    _log_text(),
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    True,
                    True,
                )

            # Entering / updating section mode.
            if position is None:
                _s_lo, _s_hi, position = section_slider_range(_dataset, pln)
            else:
                position = float(position)

            plane_changed = pln != _section_plane
            _view_mode = "section"
            _section_plane = pln
            _section_position = float(position)

            if plane_changed:
                s_lo, s_hi, s_mid = section_slider_range(_dataset, pln)
                # Keep position if still in range; otherwise jump to mid.
                if not (s_lo <= _section_position <= s_hi):
                    _section_position = s_mid
                position = _section_position
                s_step = _section_step(s_lo, s_hi)
                s_marks = _section_marks(s_lo, s_hi, position)
            else:
                s_lo = s_hi = s_step = s_marks = no_update

            fig, status = _figure_for_limit(
                _dataset,
                limit_f,
                camera=cam,
                view_mode="section",
                plane=pln,
                position=float(position),
            )
            return (
                fig,
                status,
                _log_text(),
                s_lo if plane_changed else no_update,
                s_hi if plane_changed else no_update,
                float(position) if plane_changed else no_update,
                s_step if plane_changed else no_update,
                s_marks if plane_changed else no_update,
                _section_readout(pln, float(position)),
                False,
                False,
            )
        except Exception:  # noqa: BLE001
            _append_log(traceback.format_exc())
            return (
                no_update,
                "Section update failed — see log.",
                _log_text(),
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
            )

    # Clear the old view immediately; background thread + log-poll stream progress.
    clientside_callback(
        """
        function(nClicks) {
            if (!nClicks) {
                return [
                    window.dash_clientside.no_update,
                    window.dash_clientside.no_update,
                    window.dash_clientside.no_update,
                    window.dash_clientside.no_update,
                    window.dash_clientside.no_update,
                    window.dash_clientside.no_update
                ];
            }
            const emptyFigure = {
                data: [],
                layout: {
                    title: "Extracting from RS3…",
                    margin: {l: 0, r: 0, t: 40, b: 0},
                    paper_bgcolor: "white",
                    uirevision: "fos-contour",
                    scene: {
                        aspectmode: "data",
                        bgcolor: "white",
                        uirevision: "fos-contour"
                    }
                }
            };
            return [
                emptyFigure,
                "Extracting… (log updates live)",
                "Starting new extraction…",
                null,
                false,
                0
            ];
        }
        """,
        Output("fos-graph", "figure", allow_duplicate=True),
        Output("status-bar", "children", allow_duplicate=True),
        Output("log-panel", "children", allow_duplicate=True),
        Output("camera-store", "data", allow_duplicate=True),
        Output("log-poll", "disabled", allow_duplicate=True),
        Output("log-poll", "n_intervals"),
        Input("extract-btn", "n_clicks"),
        prevent_initial_call=True,
    )

    clientside_callback(
        """
        function(relayout, current) {
            if (!relayout) { return window.dash_clientside.no_update; }
            if (relayout["scene.camera"]) { return relayout["scene.camera"]; }
            if (relayout.scene && relayout.scene.camera) {
                return relayout.scene.camera;
            }
            return window.dash_clientside.no_update;
        }
        """,
        Output("camera-store", "data"),
        Input("fos-graph", "relayoutData"),
        State("camera-store", "data"),
        prevent_initial_call=True,
    )

    return app



def run_web_viewer(
    *,
    model: Path | None = None,
    port: int = 60064,
    criterion: str = "total_displacement",
    no_start: bool = False,
    auto_extract: bool = False,
    http_port: int = _DEFAULT_HTTP_PORT,
) -> int:
    """Start Dash server and open the browser."""
    global _dataset, _suggestions, _datasets, _suggestions_by, _active_criterion

    initial = str(model.resolve()) if model is not None else ""
    initial_figure = None
    limit_min, limit_max, limit_value = 0.0, 1.0, 0.5
    status = "Load a computed .rs3v3 and click Extract."
    extract_token = 0

    if auto_extract and model is not None:
        try:
            _append_log("Auto-extract starting…")
            datasets, suggestions_by, active, initial_limit = _extract_datasets(
                str(model.resolve()),
                port,
                criterion,
                no_start=no_start,
            )
            _datasets = datasets
            _suggestions_by = suggestions_by
            _active_criterion = active
            _dataset = datasets[active]
            _suggestions = suggestions_by[active]
            limit_min, limit_max = _limit_bounds(_dataset, initial_limit)
            limit_value = initial_limit
            initial_figure, status = _figure_for_limit(_dataset, initial_limit)
            extract_token = 1
            _append_log("Auto-extract done — both criteria cached.")
        except Exception:  # noqa: BLE001
            _append_log(traceback.format_exc())
            status = "Auto-extract failed — see log. Fix RS3, then click Extract."

    app = create_app(
        initial_model=initial,
        criterion=criterion,
        port=port,
        no_start=no_start,
        initial_figure=initial_figure,
        limit_min=limit_min,
        limit_max=limit_max,
        limit_value=limit_value,
        status=status,
        extract_token=extract_token,
    )

    def open_browser():
        webbrowser.open(f"http://127.0.0.1:{http_port}")

    Timer(1.2, open_browser).start()
    print("\n" + "=" * 50)
    print("RS3 Local FoS Contour Viewer (Web)")
    print("=" * 50)
    print(f"\nStarting server at http://127.0.0.1:{http_port}")
    print("Browser will open automatically...")
    print("Press Ctrl+C to stop.\n")
    app.run(debug=False, host="127.0.0.1", port=http_port, threaded=True)
    return 0
