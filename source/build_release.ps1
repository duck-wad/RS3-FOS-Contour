# Rebuild RS3_FoS_ContourViewer and refresh ../release/
# Run from the source/ folder (this script's directory).
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$projectRoot = Split-Path $PSScriptRoot -Parent

Write-Host "Building with PyInstaller..."
python -m PyInstaller --noconfirm RS3_FoS_ContourViewer.spec
if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed with exit $LASTEXITCODE" }

$built = Join-Path $PSScriptRoot "dist\RS3_FoS_ContourViewer"
$dst = Join-Path $projectRoot "release"
$exe = Join-Path $built "RS3_FoS_ContourViewer.exe"
if (-not (Test-Path $exe)) { throw "Build output missing: $exe" }

Write-Host "Updating release\..."
New-Item -ItemType Directory -Path $dst -Force | Out-Null
if (Test-Path (Join-Path $dst "_internal")) {
    Remove-Item -Recurse -Force (Join-Path $dst "_internal")
}
if (Test-Path (Join-Path $dst "RS3_FoS_ContourViewer.exe")) {
    Remove-Item -Force (Join-Path $dst "RS3_FoS_ContourViewer.exe")
}
Copy-Item -Recurse -Force (Join-Path $built "_internal") (Join-Path $dst "_internal")
Copy-Item -Force $exe (Join-Path $dst "RS3_FoS_ContourViewer.exe")

@'
RS3 Local FoS Contour Viewer (Executable)

This folder contains a pre-built Windows executable for the RS3 Local FoS Contour Viewer.

Requirements on the target PC
1) RS3 must be installed and able to run with scripting enabled.
2) RS3 must be able to reach the scripting port (default: 60064).

How to run
1) Open the RS3 model you want to extract (optional, but recommended).
2) Run:
   RS3_FoS_ContourViewer.exe "C:\path\to\your\model.rs3v3" --auto

Optional flags:
  --port <60064>        RS3 scripting server port
  --http-port <8051>   Web UI port
  --criterion <...>    total_displacement | max_shear_strain
  --no-start            Do not try to start RS3; fail if scripting server is not running

Notes
- Keep the whole release folder together (exe + _internal). Do not move the .exe alone.
- After Extract, use View = Cross-section, then XY/XZ/YZ and the position slider.
- The first extraction can take several minutes on large models.
- The viewer spins up a local Dash/Plotly server (default http://127.0.0.1:8051).

Dev rebuild (from source\):
  powershell -ExecutionPolicy Bypass -File .\build_release.ps1
'@ | Set-Content -Encoding UTF8 (Join-Path $dst "README.txt")

$out = Get-Item (Join-Path $dst "RS3_FoS_ContourViewer.exe")
Write-Host ("Release updated: {0} ({1:N0} bytes, {2})" -f $out.FullName, $out.Length, $out.LastWriteTime)

Write-Host "Cleaning source\build\ and source\dist\..."
Remove-Item -Recurse -Force (Join-Path $PSScriptRoot "build") -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force (Join-Path $PSScriptRoot "dist") -ErrorAction SilentlyContinue
Write-Host "Done."
