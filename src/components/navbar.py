"""Build a navbar component with branding.

Variables:
    branding
    navbar_component
"""

from dash import html

from utils.constants import DATA_COLLAB_LOGO

# Create `NavLink` component that holds branding, including logo and name of app, and
# that redirects to the home page on click.
branding = html.A(
    html.Div(
        [
            html.Div(html.Img(src=DATA_COLLAB_LOGO)),
            html.Div(html.Div("Dash Test App")),
        ],
    ),
    href="/",
)

navbar_component = html.Div(branding)
