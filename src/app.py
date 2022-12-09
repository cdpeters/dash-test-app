"""Overall app layout for a multi-page application."""

import dash
import dash_bootstrap_components as dbc
from dash import Dash

from components.navbar import create_navbar_component
from utils.constants import DATA_COLLAB_LOGO, DBC_CSS, THEME

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    external_stylesheets=[THEME["cdn_url"], DBC_CSS],
    use_pages=True,
    title="Dash Test App",
)

# Place the navbar and the `page_container` for the location of page contents
app.layout = dbc.Container(
    [
        create_navbar_component(
            page_registry=dash.page_registry, brand_logo=DATA_COLLAB_LOGO
        ),
        # Location for page contents.
        dash.page_container,
    ],
    class_name="dbc px-0 vh-100",
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
