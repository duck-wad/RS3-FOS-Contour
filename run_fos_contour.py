"""
Build a FLAC-style local Factor of Safety contour from an RS3 SSR model.

Examples
--------
Suggest a limiting value from the critical SRF displacement field:

    python run_fos_contour.py "model.rs3v3" --suggest-limit

Compute local FoS using total displacement and an absolute limit:

    python run_fos_contour.py "model.rs3v3" ^
        --criterion total_displacement ^
        --mode absolute ^
        --limit 0.01 ^
        --out local_fos.csv

Use max shear strain with incremental thresholding:

    python run_fos_contour.py "model.rs3v3" ^
        --criterion max_shear_strain ^
        --mode incremental ^
        --limit 1e-4 ^
        --out local_fos.csv

By default the script attaches to a running RS3 scripting server if one
is already on --port, and reuses the model if it is already open.
Otherwise it starts RS3 and opens the file.

    python run_fos_contour.py "model.rs3v3" --suggest-limit
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extract RS3 SSR nodal results and build a local FoS "
            "(safety-map) point cloud, analogous to FLAC FoS contours. "
            "Attaches to a running RS3 session when available."
        )
    )
    parser.add_argument(
        "model",
        type=Path,
        help="Path to the computed .rs3v3 model (SSR results required).",
    )
    parser.add_argument(
        "--criterion",
        default="total_displacement",
        help="Kinematic field: total_displacement | max_shear_strain",
    )
    parser.add_argument(
        "--mode",
        default="absolute",
        help="Threshold mode: absolute | incremental",
    )
    parser.add_argument(
        "--limit",
        type=float,
        default=None,
        help="User-defined limiting value. Required unless --suggest-limit.",
    )
    parser.add_argument(
        "--suggest-limit",
        action="store_true",
        help="Print suggested limits from the critical SRF field and exit.",
    )
    parser.add_argument(
        "--stage",
        type=int,
        default=1,
        help="1-based stage number (default: 1).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("local_fos.csv"),
        help="Output CSV path for the local FoS point cloud.",
    )
    parser.add_argument(
        "--srf-summary",
        type=Path,
        default=None,
        help="Optional CSV path for the SRF trial table.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=60064,
        help="RS3 scripting server port (default: 60064).",
    )
    parser.add_argument(
        "--no-start",
        action="store_true",
        help=(
            "Never launch RS3; fail if no scripting server is listening "
            "on --port. Default behavior already attaches when RS3 is up."
        ),
    )
    parser.add_argument(
        "--keep-open",
        action="store_true",
        help=(
            "Leave RS3 / the model open after the script finishes. "
            "Implied when attaching to an already-running RS3 session."
        ),
    )
    parser.add_argument(
        "--entity",
        default=None,
        help="Optional external volume / entity name filter for mesh queries.",
    )
    parser.add_argument(
        "--surface-only",
        action="store_true",
        help=(
            "Keep free-surface / near-surface nodes only. "
            "Default keeps the full volume (needed for cross-section models)."
        ),
    )
    parser.add_argument(
        "--surface-mode",
        default="map",
        help=(
            "With --surface-only: map (exclude box bottom/sides) | "
            "boundary | topo."
        ),
    )
    parser.add_argument(
        "--shell-depth",
        type=float,
        default=0.0,
        help="With --surface-only: extra near-surface thickness (default: 0).",
    )
    parser.add_argument(
        "--surface-layers",
        type=int,
        default=1,
        help="With --surface-only: extra element rings under the free surface.",
    )
    parser.add_argument(
        "--max-points",
        type=int,
        default=None,
        help="Optional cap on retained nodes (spatial decimation).",
    )
    parser.add_argument(
        "--open-timeout",
        type=float,
        default=180.0,
        help="Seconds to wait for model open / attach (default: 180).",
    )
    parser.add_argument(
        "--rpc-timeout",
        type=float,
        default=300.0,
        help=(
            "Seconds per mesh-result RPC before aborting (default: 300). "
            "Use 0 to disable."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    model_path = args.model.resolve()
    if not model_path.exists():
        print(f"Model not found: {model_path}", file=sys.stderr)
        return 1

    if args.limit is None and not args.suggest_limit:
        print(
            "Provide --limit, or use --suggest-limit to inspect candidate thresholds.",
            file=sys.stderr,
        )
        return 1

    from fos_contour.criteria import parse_criterion, parse_failure_mode
    from fos_contour.export import export_csv, export_srf_summary, suggest_limit
    from fos_contour.local_fos import compute_local_fos
    from fos_contour.rs3_extract import extract_nodal_histories, list_srf_trials
    from fos_contour.session import connect_model

    criterion = parse_criterion(args.criterion)
    failure_mode = parse_failure_mode(args.mode)

    rpc_timeout = None if args.rpc_timeout <= 0 else args.rpc_timeout

    session = None
    try:
        session = connect_model(
            model_path,
            port=args.port,
            force_no_start=args.no_start,
            open_timeout_s=args.open_timeout,
            progress_callback=print,
        )
        model = session.model

        trials = list_srf_trials(model)
        print(f"Found {len(trials)} SRF result(s):", flush=True)
        for trial in trials:
            flag = "converged" if trial.converged else "NOT converged"
            print(
                f"  [{trial.index}] SRF={trial.srf:g}  "
                f"max|u|={trial.max_total_displacement:g}  ({flag})",
                flush=True,
            )

        if args.srf_summary is not None:
            path = export_srf_summary(trials, args.srf_summary)
            print(f"Wrote SRF summary: {path}", flush=True)

        print(
            f"Extracting nodal {criterion.value} histories "
            f"(stage={args.stage})...",
            flush=True,
        )
        used_trials, histories = extract_nodal_histories(
            model,
            criterion=criterion,
            stage_number=args.stage,
            entity_name=args.entity,
            rpc_timeout_s=rpc_timeout,
            surface_only=args.surface_only,
            surface_mode=args.surface_mode,
            shell_depth=args.shell_depth,
            surface_layers=args.surface_layers,
            max_points=args.max_points,
            progress_callback=print,
        )
        print(f"Nodes collected: {len(histories)}")

        suggestions = suggest_limit(
            used_trials,
            histories,
            failure_mode=failure_mode,
        )
        print("Limit suggestions (tune like FLAC limiting velocity):")
        for key, value in suggestions.items():
            print(f"  {key}: {value:g}")

        if args.suggest_limit:
            return 0

        result = compute_local_fos(
            used_trials,
            histories,
            limit=args.limit,
            criterion=criterion,
            failure_mode=failure_mode,
            stage_number=args.stage,
        )
        out = export_csv(result, args.out)
        failed_count = sum(1 for p in result.points if p.failed)
        print(
            f"Wrote {len(result.points)} points to {out} "
            f"({failed_count} nodes exceeded limit)."
        )
        if result.global_min_fos is not None:
            print(f"Minimum local FoS among failed nodes: {result.global_min_fos:g}")
        return 0
    finally:
        if session is not None:
            # Keep the user's live RS3 session intact when we only attached.
            keep_open = (
                args.keep_open
                or session.model_was_already_open
                or not session.started_application
            )
            session.close(keep_open=keep_open)


if __name__ == "__main__":
    raise SystemExit(main())
