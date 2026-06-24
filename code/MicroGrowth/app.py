import sys
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent  # .../code/MicroGrowth

# Streamlit only auto-adds the entrypoint script's directory to sys.path. When
# launched via code/streamlit_app.py that directory is code/, not this one, so
# add MicroGrowth ourselves to keep `from src...` imports working.
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.styling import green_gradient, green_navbar, red_buttons

APP_VERSION = (BASE_DIR / "VERSION").read_text(encoding="utf-8").strip()

try:
    from growthcurve_app import __version__ as PACKAGE_VERSION
except Exception:
    PACKAGE_VERSION = "not-installed"

LOGO = str(BASE_DIR / "logo.svg")

st.set_page_config(
    page_title="MicroGrowth",
    layout="wide",
    page_icon=LOGO,
    initial_sidebar_state="collapsed",
)

with st.sidebar:
    st.caption(f"MicroGrowth app v{APP_VERSION}")
    st.caption(f"growthcurve_app package v{PACKAGE_VERSION}")

# Display logo (will stay visible even when sidebar is collapsed)
st.logo(
    LOGO,
    link="https://github.com/biosustain/growthcurves_app/tree/main/MicroGrowth",
)


nav = st.navigation(
    [
        st.Page(BASE_DIR / "src/pages/upload_and_analyse.py", title="Upload & Analyse"),
        st.Page(BASE_DIR / "src/pages/plate_overviews.py", title="Plate Overviews"),
        st.Page(BASE_DIR / "src/pages/check_growth_fits.py", title="Check Growth Fits"),
        st.Page(BASE_DIR / "src/pages/create_visualizations.py", title="Create Visualizations"),
        st.Page(BASE_DIR / "src/pages/download_analyzed_data.py", title="Download Analyzed Data"),
    ],
    position="top",
)

red_buttons()
green_gradient()
green_navbar()

nav.run()
