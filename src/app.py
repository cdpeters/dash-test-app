"""Overall app layout for a multi-page application."""

import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State

from components.navbar import navbar
from utils.constants import (
    DATA_COLLAB_LOGO,
    DBC_CSS,
    NAVBAR_COLLAPSE,
    NAVBAR_TOGGLER,
    THEME,
)

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
        navbar(page_registry=dash.page_registry, brand_logo=DATA_COLLAB_LOGO),
        # Location for page contents.
        dash.page_container,
    ],
    class_name="dbc px-0 vh-100",
    fluid=True,
)


# A callback for toggling the collapsible menu of page links when the screen size is
# small.
@app.callback(
    Output(NAVBAR_COLLAPSE, "is_open"),
    Input(NAVBAR_TOGGLER, "n_clicks"),
    State(NAVBAR_COLLAPSE, "is_open"),
)
def toggle_navbar_collapse(n_clicks, is_open):
    """Toggle the collapse of the navbar page links dropdown at small screen sizes."""
    if n_clicks:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)
