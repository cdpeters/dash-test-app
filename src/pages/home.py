"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import HOME_PAGE_ICON

# Needed for the app to see this module as a page.
register_page(__name__, path="/", sidebar=True, icon_path=HOME_PAGE_ICON)

layout = html.Div(
    html.Div(
        "Welcome to the Dash Test App",
        className="text-5xl xl:text-6xl pb-40 text-slate-700",
    ),
    className="""flex items-center justify-center h-screen""",
)
