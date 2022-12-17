"""Build a navbar component with branding.

Variables:
    branding
    navbar_component
"""

import dash_bootstrap_components as dbc
from dash import html

from utils.constants import DATA_COLLAB_LOGO

# Create `NavLink` component that holds branding, including logo and name of app, and
# that redirects to the home page on click.
branding = dbc.NavLink(
    dbc.Row(
        [
            dbc.Col(html.Img(src=DATA_COLLAB_LOGO, height="30px")),
            dbc.Col(dbc.NavbarBrand("Dash Test App", className="ms-2")),
        ],
        align="center",
        className="g-0",
    ),
    class_name="py-0 px-1",
    href="/",
    style={"textDecoration": "none"},
)

navbar_component = dbc.Navbar(
    branding,
    color="primary",
    dark=True,
    class_name="d-flex justify-content-start px-2",
)
