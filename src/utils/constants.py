"""Constants used throughout the app.

Constants are in all caps. Variables that set the constants are all lowercase.
"""

import dash_bootstrap_components.themes as dbc_themes

# Theme Selection ----------------------------------------------------------------------
# `THEME_NAME` is only used in this file.
THEME_NAME = "minty"
THEME = {"name": THEME_NAME, "cdn_url": getattr(dbc_themes, THEME_NAME.upper())}

# Navbar Brand Logo --------------------------------------------------------------------
DATA_COLLAB_LOGO = "/assets/data_collab.png"

# Stylesheet For DCC Components --------------------------------------------------------
# Stylesheet for styling dash core components using the `className="dbc"` argument
# applied to the outer container of a layout. See
# https://github.com/AnnMarieW/dash-bootstrap-templates for usage.
DBC_CSS = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
)

# Ids ----------------------------------------------------------------------------------
FIGURE_BAR = "figure-bar"
FIGURE_TEMP = "figure-temp"
FIGURE_PRCP = "figure-prcp"
TABLE = "table-01"
NAVBAR_TOGGLER = "navbar-toggler"
NAVBAR_COLLAPSE = "navbar-collapse"
