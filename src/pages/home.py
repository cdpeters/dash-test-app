"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import HOME_ICON_DARK, HOME_ICON_LIGHT, ID_HOME_ICON, ID_HOME_LINK

# Needed for the app to see this module as a page.
register_page(
    __name__,
    path="/",
    sidebar=True,
    order=0,
    id_icon=ID_HOME_ICON,
    id_link=ID_HOME_LINK,
    icon_light=HOME_ICON_LIGHT,
    icon_dark=HOME_ICON_DARK,
)

layout = html.Div(
    html.Div(
        "Welcome to the Dash Test App",
        className="text-5xl pb-40 text-slate-700 xl:text-6xl",
    ),
    className="flex items-center justify-center h-screen",
)
