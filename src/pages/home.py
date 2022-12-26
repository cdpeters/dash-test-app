"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

# Needed for the app to see this module as a page.
register_page(__name__, path="/")

layout = html.Div(
    [
        html.H1(
            "Welcome to the Dash Test App",
        ),
    ],
)
