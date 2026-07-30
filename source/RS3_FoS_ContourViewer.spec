# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for RS3 FoS Contour Viewer."""

from PyInstaller.utils.hooks import collect_all, collect_submodules

datas = []
binaries = []
hiddenimports = []

# RS3 protobuf stubs need the full package on disk / importable as submodules.
rs3_datas, rs3_binaries, rs3_hidden = collect_all("rs3")
datas += rs3_datas
binaries += rs3_binaries
hiddenimports += rs3_hidden
hiddenimports += collect_submodules("rs3")
hiddenimports += collect_submodules("google.protobuf")
hiddenimports += ["fos_contour.rs3_bootstrap"]

a = Analysis(
    ["run_fos_viewer.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=["packaging/pyi_rth_rs3_pb2.py"],
    excludes=[
        "pyvista",
        "vtk",
        "vtkmodules",
        "PySide6",
        "PyQt5",
        "PyQt6",
        "qtpy",
        "pandas",
        "matplotlib",
        "IPython",
        "notebook",
        "scipy",
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="RS3_FoS_ContourViewer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="RS3_FoS_ContourViewer",
)
