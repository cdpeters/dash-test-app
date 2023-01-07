"""Layout for the home page.

Variables:
    layout
"""

import dash_bootstrap_components as dbc
from dash import html, register_page

# Needed for the app to see this module as a page.
register_page(__name__, path="/")

layout = dbc.Container(
    [
        html.H1(
            "Welcome to the Dash Test App",
            className="display-4 fw-bold mt-5 pt-4",
            style={"textAlign": "center"},
        ),
    ],
    fluid=True,
    className="d-flex align-content-center justify-content-center",
)
