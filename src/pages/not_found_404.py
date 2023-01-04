"""Layout when user navigates to a route that doesn't exist.

Variables:
    layout
"""

from dash import html, register_page

register_page(__name__)

layout = html.Div(
    html.Div(
        """This page does not exist. Please use the page links in the sidebar to
        navigate the website.""",
        className="text-lg text-slate-700",
    ),
    className="flex items-center justify-center h-screen",
)
