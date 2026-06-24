"""Code Ocean entrypoint.

Code Ocean requires a streamlit_app.py in /code. The real MicroGrowth app
lives in MicroGrowth/app.py and relies on cwd-relative asset paths (e.g.
"MicroGrowth/logo.svg"), so we pin the working directory to this file's
directory and execute the app with __file__ pointing at the real module.
"""

import os
import sys
from pathlib import Path

CODE_DIR = Path(__file__).parent
APP_DIR = CODE_DIR / "MicroGrowth"

# Ensure cwd == code/ so "MicroGrowth/..." asset paths resolve regardless of
# how Code Ocean invokes this script.
os.chdir(CODE_DIR)

# Make `from src...` imports inside the app resolve.
sys.path.insert(0, str(APP_DIR))

app_file = APP_DIR / "app.py"
code = compile(app_file.read_text(encoding="utf-8"), str(app_file), "exec")
exec(code, {"__file__": str(app_file), "__name__": "__main__"})
