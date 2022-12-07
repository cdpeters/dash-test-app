"""Constants used throughout the app.

A `secrets.toml` file is also read and the appropriate constants are assigned.
"""

from pathlib import Path

import dash_bootstrap_components.themes as dbc_themes
import tomli

# Data Directories ---------------------------------------------------------------------
# Use the file path (`__file__`) of this module to form the paths to both the google
# drive collaboration folder and to the project's data directory. `parents[2]` is the
# 3rd parent (since index 2 is 3rd element) of the file path for this module: the
# project's root directory dash-test-app.
with open(Path(__file__).parents[2] / "secrets.toml", "rb") as f:
    secrets = tomli.load(f)
GOOGLE_DRIVE_DIR = Path(secrets["google_drive"]["path"])
DATA_DIR = Path(__file__).parents[2] / "data"

# Theme Selection ----------------------------------------------------------------------
# `THEME_NAME` is only used in this file.
theme_name = "minty"
THEME = {"name": theme_name, "cdn_url": getattr(dbc_themes, theme_name.upper())}

# Navbar Brand Logo --------------------------------------------------------------------
DATA_COLLAB_LOGO = "/assets/data_collab.png"

# Stylesheet For DCC Components --------------------------------------------------------
# Stylesheet for styling dash core components using the `className="dbc"` argument
# applied to the outer container of a layout. See
# https://github.com/AnnMarieW/dash-bootstrap-templates for usage.
DBC_CSS = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
)

# Component Ids ------------------------------------------------------------------------
FIGURE_BAR = "figure-bar"
FIGURE_TEMP = "figure-temp"
FIGURE_PRCP = "figure-prcp"
TABLE = "table-01"
NAVBAR_TOGGLER = "navbar-toggler"
NAVBAR_COLLAPSE = "navbar-collapse"
