"""Constants used throughout the app.

A `secrets.toml` file is loaded via the `tomli` library and the appropriate constants
are assigned. Additional constants (not contained within `secrets.toml`) are also
defined.

Constants:
    Data Directories:
        GOOGLE_DRIVE_DIR: Path to shared google drive collaboration folder.
        DATA_DIR: Path to the `data` directory in the project root (`dash-test-app`).

    Theme Selection:
        THEMES: Contains the name and cdn_url's for all the available bootstrap themes.
        DEFAULT_THEME

    Stylesheets:
        DBC_CSS: Stylesheet that yields the `dbc` class for outer container of app.

    Brand Logo:
        DATA_COLLAB_LOGO

    Component Ids:
        FIGURE_BAR
        FIGURE_TEMP
        FIGURE_PRECIP
        TABLE_CLIMATE
        NAVBAR_TOGGLER
        NAVBAR_COLLAPSE
"""

from pathlib import Path

import dash_bootstrap_components.themes as dbc_themes
import tomli

# Data Directories ---------------------------------------------------------------------

# Use the file path (`__file__`) of this module to form the paths to both the google
# drive collaboration folder and to the project's data directory. `parents[2]` is the
# 3rd parent (since index 2 is 3rd element) of the file path for this module: the
# project's root directory `dash-test-app`.
with open(Path(__file__).parents[2] / "secrets.toml", "rb") as f:
    secrets = tomli.load(f)

GOOGLE_DRIVE_DIR = Path(secrets["google_drive"]["path"])
DATA_DIR = Path(__file__).parents[2] / "data"


# Theme Selection ----------------------------------------------------------------------

# `theme_name` is only used in this file.
# templates = [BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA,
# LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE,
# SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR]
theme_names = [
    item for item in dir(dbc_themes) if (not item.startswith("_")) and item != "GRID"
]

THEMES: dict[str, dict[str, str]] = {
    theme_name: {"name": theme_name.lower(), "cdn_url": getattr(dbc_themes, theme_name)}
    for theme_name in theme_names
}

DEFAULT_THEME = THEMES["MINTY"]


# Stylesheets --------------------------------------------------------------------------

# Stylesheet for styling dash core components (dcc) using the `className="dbc"` argument
# applied to the outer container of a layout. See
# https://github.com/AnnMarieW/dash-bootstrap-templates for usage.
DBC_CSS = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
)


# Brand Logo ---------------------------------------------------------------------------

DATA_COLLAB_LOGO = "/assets/data_collab.png"


# Component Ids ------------------------------------------------------------------------

FIGURE_BAR = "figure-bar"
FIGURE_TEMP = "figure-temp"
FIGURE_PRECIP = "figure-prcp"
TABLE_CLIMATE = "table-01"
NAVBAR_TOGGLER = "navbar-toggler"
NAVBAR_COLLAPSE = "navbar-collapse"
