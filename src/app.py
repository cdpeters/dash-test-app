"""Overall app layout for a multi-page application.

Variables:
    app
"""

import dash
import dash_bootstrap_components as dbc
from dash import Dash

from components.navbar import create_navbar_component
from utils.constants import DBC_CSS, DEFAULT_THEME

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    external_stylesheets=[DEFAULT_THEME["cdn_url"], DBC_CSS],
    use_pages=True,
    title="Dash Test App",
)

# Place the navbar and the container for page content within the app.
app.layout = dbc.Container(
    [
        create_navbar_component(page_registry=dash.page_registry),
        # Location for page contents.
        dash.page_container,
    ],
    class_name="dbc px-0 vh-100",
    fluid=True,
)

if __name__ == "__main__":
    app.run(debug=True)
