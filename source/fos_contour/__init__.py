"""
FLAC-style Factor of Safety (local SRF) contour post-processing for RS3.

Reconstructs a per-node local FoS field from intermediate Shear Strength
Reduction (SSR) results by thresholding total displacement or max shear strain.
"""

from .criteria import Criterion, FailureMode
from .dataset import ContourDataset, histories_to_dataset
from .local_fos import LocalFoSResult, compute_local_fos
from .rs3_extract import SRFTrial, extract_nodal_histories, list_srf_trials
from .export import export_csv, suggest_limit
from .session import RS3Session, connect_model
from .surface import SurfaceSelection, select_surface_nodes

__all__ = [
    "ContourDataset",
    "Criterion",
    "FailureMode",
    "LocalFoSResult",
    "RS3Session",
    "SRFTrial",
    "SurfaceSelection",
    "compute_local_fos",
    "connect_model",
    "extract_nodal_histories",
    "histories_to_dataset",
    "list_srf_trials",
    "export_csv",
    "select_surface_nodes",
    "suggest_limit",
]
