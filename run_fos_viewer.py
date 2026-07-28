"""
Launch the interactive RS3 Local FoS contour viewer (web / Dash).

Opens in the browser with WebGL Mesh3d contours (same stack as
RS3 Compute Analyzer).

Examples
--------
    python run_fos_viewer.py

    python run_fos_viewer.py "Joint slope stability SSR - final.rs3v3" --auto
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Interactive RS3 local FoS contour viewer (web)."
    )
    parser.add_argument(
        "model",
        nargs="?",
        type=Path,
        default=None,
        help="Optional path to a computed .rs3v3 model.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=60064,
        help="RS3 scripting server port (default: 60064).",
    )
    parser.add_argument(
        "--http-port",
        type=int,
        default=8051,
        help="Local web server port (default: 8051).",
    )
    parser.add_argument(
        "--criterion",
        default="total_displacement",
        help="total_displacement | max_shear_strain",
    )
    parser.add_argument(
        "--no-start",
        action="store_true",
        help="Do not launch RS3 if no scripting server is running.",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="If a model path is given, extract before opening the browser.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    model = args.model.resolve() if args.model is not None else None
    if model is not None and not model.exists():
        print(f"Model not found: {model}", file=sys.stderr)
        return 1

    # Frozen builds: RS3 protobuf stubs use bare imports that need aliases.
    from fos_contour.rs3_bootstrap import ensure_rs3_protobuf_imports

    ensure_rs3_protobuf_imports()

    from fos_contour.web_app import run_web_viewer

    return run_web_viewer(
        model=model,
        port=args.port,
        criterion=args.criterion,
        no_start=args.no_start,
        auto_extract=bool(args.auto and model is not None),
        http_port=args.http_port,
    )


if __name__ == "__main__":
    raise SystemExit(main())
