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
        BACKGROUND_PAGE_ICON
        DASHBOARD_PAGE_ICON
        DATA_COLLAB_LOGO
        GITHUB_ICON
        HOME_PAGE_ICON

    Component Ids:
        FIGURE_BAR
        FIGURE_TEMP
        FIGURE_PRECIP
        TABLE_CLIMATE
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

BACKGROUND_PAGE_ICON = "/assets/images/book.svg"
DASHBOARD_PAGE_ICON = "/assets/images/chart-line.svg"
DATA_COLLAB_LOGO = "/assets/images/data_collab.png"
GITHUB_ICON = "/assets/images/github.svg"
HOME_PAGE_ICON = "/assets/images/house.svg"


# Component Ids ------------------------------------------------------------------------

FIGURE_BAR = "figure-bar"
FIGURE_TEMP = "figure-temp"
FIGURE_PRECIP = "figure-prcp"
TABLE_CLIMATE = "table-01"
