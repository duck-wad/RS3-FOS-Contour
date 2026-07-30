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
