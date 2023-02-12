"""Build a sidebar component with page links.

The create sidebar function takes in the page registry and builds page links. There is
also a header that redirects to the home page of the app.

Functions:
    create_sidebar_component
"""
import re

from dash import Input, Output, State, callback, dcc, html, page_registry

from utils.constants import (
    BG_COLOR_DARK,
    BG_COLOR_LIGHT,
    HOVER_COLOR_DARK,
    ID_BACKGROUND_ICON,
    ID_BACKGROUND_LINK,
    ID_DASHBOARD_ICON,
    ID_DASHBOARD_LINK,
    ID_HOME_ICON,
    ID_HOME_LINK,
    ID_LOCATION,
    TEXT_COLOR_DARK,
    TEXT_COLOR_LIGHT,
)
from utils.funcs import update_utility_classes


def create_sidebar_component() -> html.Div:
    """Create the sidebar component with page links for navigation.

    `page_registry` page data is used to construct the sidebar's page links. A page is
    included if it has a `sidebar` key with a value of True set when the page was
    registered.

    Returns
    -------
    html.Div
        A sidebar with a link to each page.
    """
    heading = dcc.Link(
        [
            html.Div(
                "Dash Test App",
                className="py-3 text-center font-semibold text-emerald-50",
            ),
        ],
        href="/",
    )

    page_links = [
        dcc.Link(
            [
                html.Img(
                    id=page["id_icon"],
                    src=page["icon_light"],
                    className="aspect-square w-3",
                ),
                html.Div(page["name"], className="text-sm text-inherit bg-inherit"),
            ],
            id=page["id_link"],
            href=page["relative_path"],
            className="""px-4 py-2 flex space-x-2 items-center bg-slate-800
            text-emerald-50 hover:bg-slate-700 """,
        )
        for page in page_registry.values()
        if page.get("sidebar")
    ]

    return html.Div(
        # `page_links` has to be unpacked since it is a list (i.e. the `children`
        # argument can be a list but it must not contain a list as an element).
        [
            dcc.Location(id=ID_LOCATION, refresh=False),
            heading,
            *page_links,
        ],
        className="bg-slate-800 h-screen w-32 fixed overflow-auto",
    )


@callback(
    output={
        "output_icon_src": {
            "home": Output(component_id=ID_HOME_ICON, component_property="src"),
            "background": Output(
                component_id=ID_BACKGROUND_ICON, component_property="src"
            ),
            "dashboard": Output(
                component_id=ID_DASHBOARD_ICON, component_property="src"
            ),
        },
        "output_link_class": {
            "home": Output(component_id=ID_HOME_LINK, component_property="className"),
            "background": Output(
                component_id=ID_BACKGROUND_LINK, component_property="className"
            ),
            "dashboard": Output(
                component_id=ID_DASHBOARD_LINK, component_property="className"
            ),
        },
    },
    inputs={
        "pathname": Input(component_id=ID_LOCATION, component_property="pathname"),
        "input_icon_src": {
            "home": State(component_id=ID_HOME_ICON, component_property="src"),
            "background": State(
                component_id=ID_BACKGROUND_ICON, component_property="src"
            ),
            "dashboard": State(
                component_id=ID_DASHBOARD_ICON, component_property="src"
            ),
        },
        "input_link_class": {
            "home": State(component_id=ID_HOME_LINK, component_property="className"),
            "background": State(
                component_id=ID_BACKGROUND_LINK, component_property="className"
            ),
            "dashboard": State(
                component_id=ID_DASHBOARD_LINK, component_property="className"
            ),
        },
    },
)
def update_page_link_styling(pathname, input_icon_src, input_link_class):
    """Update icons and link colors when a link is active.

    Parameters
    ----------
    pathname : str
        Current pathname of the app.
    input_icon_src : dict[str, str]
        Contains the src attribute for each page link's icon.
    input_link_class : dict[str, str]
        Contains the class attribute for each page link.

    Returns
    -------
    dict[str, dict[str, str]]
        Contains the updated icon src attributes and page link class attributes.
    """
    home_page = page_registry["pages.home"]
    background_page = page_registry["pages.background"]
    dashboard_page = page_registry["pages.dashboard"]

    # Assign icon src attribute variables that will be updated below if necessary.
    home_icon_src = input_icon_src["home"]
    background_icon_src = input_icon_src["background"]
    dashboard_icon_src = input_icon_src["dashboard"]
    # Assign page link class attribute variables that will be updated below if
    # necessary.
    home_link_class = input_link_class["home"]
    background_link_class = input_link_class["background"]
    dashboard_link_class = input_link_class["dashboard"]

    # Capture the color of the icon from the icon's src attribute for each page.
    pattern = r"_([a-z]+)\."
    icon_color = {
        page: re.search(pattern, icon_src).group(1)
        for page, icon_src in input_icon_src.items()
    }

    # Update the color of the icon and the color styling of the link as a whole
    # (background color and text color) based on the current pathname.
    if pathname == home_page["relative_path"]:
        if icon_color["home"] != "dark":
            home_icon_src = home_page["icon_dark"]
            home_link_class = update_utility_classes(
                current_classes=home_link_class,
                remove_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
                add_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
            )
        if icon_color["background"] == "dark":
            background_icon_src = background_page["icon_light"]
            background_link_class = update_utility_classes(
                current_classes=background_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
        if icon_color["dashboard"] == "dark":
            dashboard_icon_src = dashboard_page["icon_light"]
            dashboard_link_class = update_utility_classes(
                current_classes=dashboard_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
    elif pathname == background_page["relative_path"]:
        if icon_color["home"] == "dark":
            home_icon_src = home_page["icon_light"]
            home_link_class = update_utility_classes(
                current_classes=home_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
        if icon_color["background"] != "dark":
            background_icon_src = background_page["icon_dark"]
            background_link_class = update_utility_classes(
                current_classes=background_link_class,
                remove_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
                add_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
            )
        if icon_color["dashboard"] == "dark":
            dashboard_icon_src = dashboard_page["icon_light"]
            dashboard_link_class = update_utility_classes(
                current_classes=dashboard_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
    elif pathname == dashboard_page["relative_path"]:
        if icon_color["home"] == "dark":
            home_icon_src = home_page["icon_light"]
            home_link_class = update_utility_classes(
                current_classes=home_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
        if icon_color["background"] == "dark":
            background_icon_src = background_page["icon_light"]
            background_link_class = update_utility_classes(
                current_classes=background_link_class,
                remove_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
                add_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
            )
        if icon_color["dashboard"] != "dark":
            dashboard_icon_src = dashboard_page["icon_dark"]
            dashboard_link_class = update_utility_classes(
                current_classes=dashboard_link_class,
                remove_classes=[BG_COLOR_DARK, TEXT_COLOR_LIGHT, HOVER_COLOR_DARK],
                add_classes=[BG_COLOR_LIGHT, TEXT_COLOR_DARK],
            )

    return {
        "output_icon_src": {
            "home": home_icon_src,
            "background": background_icon_src,
            "dashboard": dashboard_icon_src,
        },
        "output_link_class": {
            "home": home_link_class,
            "background": background_link_class,
            "dashboard": dashboard_link_class,
        },
    }
