"""Constants used throughout the app.

A `secrets.toml` file is loaded via the `tomli` library and the appropriate constants
are assigned. Additional constants (not contained within `secrets.toml`) are also
defined.

Constants:
    Data Directories:
        GOOGLE_DRIVE_DIR: Path to shared google drive collaboration folder.
        DATA_DIR: Path to the `data` directory in the project root (`dash-test-app`).

    External Links:
        APP_SOURCE_CODE_URL

    Logos and Icons:
        BACKGROUND_ICON_DARK
        BACKGROUND_ICON_LIGHT
        DASHBOARD_ICON_DARK
        DASHBOARD_ICON_LIGHT
        DATA_COLLAB_LOGO
        GITHUB_ICON
        HOME_ICON_DARK
        HOME_ICON_LIGHT

    Frequently Used CSS Classes:
        BG_COLOR_PREFIX
        BG_COLOR_DARK
        BG_COLOR_LIGHT
        TEXT_COLOR_PREFIX
        TEXT_COLOR_DARK
        TEXT_COLOR_LIGHT
        HOVER_COLOR_DARK

    Component Ids:
        ID_BACKGROUND_ICON
        ID_BACKGROUND_LINK
        ID_DASHBOARD_ICON
        ID_DASHBOARD_LINK
        ID_FIGURE_BAR
        ID_FIGURE_TEMP
        ID_FIGURE_PRECIP
        ID_HOME_ICON
        ID_HOME_LINK
        ID_LOCATION
        ID_TABLE_CLIMATE
"""

from pathlib import Path

import tomli

# Load secrets.toml --------------------------------------------------------------------

# Use the file path (`__file__`) of this module to form the paths to both the google
# drive collaboration folder and to the project's data directory. `parents[2]` is the
# 3rd parent (since index 2 is 3rd element) of the file path for this module: the
# project's root directory `dash-test-app`.
with open(Path(__file__).parents[2] / "secrets.toml", "rb") as f:
    secrets = tomli.load(f)


# Data Directories ---------------------------------------------------------------------

GOOGLE_DRIVE_DIR = Path(secrets["google_drive"]["path"])
DATA_DIR = Path(__file__).parents[2] / "data"


# External Links -----------------------------------------------------------------------

APP_SOURCE_CODE_URL = "https://github.com/cdpeters/dash-test-app"


# Logos and Icons ----------------------------------------------------------------------

BACKGROUND_ICON_DARK = "/assets/images/book_dark.svg"
BACKGROUND_ICON_LIGHT = "/assets/images/book_light.svg"
DASHBOARD_ICON_DARK = "/assets/images/chart-line_dark.svg"
DASHBOARD_ICON_LIGHT = "/assets/images/chart-line_light.svg"
DATA_COLLAB_LOGO = "/assets/images/data_collab.png"
GITHUB_ICON = "/assets/images/github.svg"
HOME_ICON_DARK = "/assets/images/house_dark.svg"
HOME_ICON_LIGHT = "/assets/images/house_light.svg"


# Frequently Used CSS Classes ----------------------------------------------------------
BG_COLOR_PREFIX = "bg"
BG_COLOR_DARK = "bg-slate-800"
BG_COLOR_LIGHT = "bg-emerald-50"
TEXT_COLOR_PREFIX = "text"
TEXT_COLOR_DARK = "text-slate-800"
TEXT_COLOR_LIGHT = "text-emerald-50"
HOVER_COLOR_DARK = "hover:bg-slate-700"


# Component Ids ------------------------------------------------------------------------

ID_BACKGROUND_ICON = "background-icon"
ID_BACKGROUND_LINK = "background-link"
ID_DASHBOARD_ICON = "dashboard-icon"
ID_DASHBOARD_LINK = "dashboard-link"
ID_FIGURE_BAR = "figure-bar"
ID_FIGURE_TEMP = "figure-temp"
ID_FIGURE_PRECIP = "figure-precip"
ID_HOME_ICON = "home-icon"
ID_HOME_LINK = "home-link"
ID_LOCATION = "location"
ID_TABLE_CLIMATE = "table-climate"
