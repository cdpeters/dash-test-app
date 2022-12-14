"""Layout when user navigates to a route that doesn't exist.

Variables:
    layout
"""

import dash
from dash import html

dash.register_page(__name__)

layout = html.H4(
    "This page does not exist. Please use the page links to navigate the website."
)
