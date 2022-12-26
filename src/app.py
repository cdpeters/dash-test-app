"""Overall app layout for a multi-page application.

Variables:
    app
"""

import dash
from dash import Dash, html

from components.navbar import navbar_component
from components.sidebar import create_sidebar_component

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    # external_scripts=[TAILWIND_CDN],
    use_pages=True,
    title="Dash Test App",
    assets_ignore="input.css",
)

# Place the navbar and the container for page content within the app.
app.layout = html.Div(
    [
        html.Div(
            create_sidebar_component(page_registry=dash.page_registry),
            className="bg-pink-400",
        ),
        # Hidden sidebar sized div to move the navbar and content out from under the
        # sidebar.
        html.Div(),
        html.Div(
            [
                navbar_component,
                # Location for page contents.
                dash.page_container,
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
