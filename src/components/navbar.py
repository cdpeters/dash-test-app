"""Build a navbar component with page links and branding.

Functions are created to build a navbar component for the main app layout. A callback is
created to control navbar collapse functionality for small screen sizes.

Variables:
    brand_component
Functions:
    create_page_link_component
    create_navbar_component
Callbacks:
    toggle_navbar_collapse
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html

from utils.constants import DATA_COLLAB_LOGO, NAVBAR_COLLAPSE, NAVBAR_TOGGLER

if TYPE_CHECKING:
    from collections import OrderedDict

# Create `NavLink` component that holds branding, including logo and name of app, and
# that redirects to the home page on click.
brand_component = dbc.NavLink(
    dbc.Row(
        [
            # Brand logo.
            dbc.Col(html.Img(src=DATA_COLLAB_LOGO, style={"height": "30px"})),
            # App name.
            dbc.Col(dbc.NavbarBrand("Dash Test App", class_name="mx-2")),
        ],
        align="center",
        class_name="g-0",
    ),
    href="/",
    class_name="ps-0 py-0",
)


def create_page_link_component(
    page_registry: OrderedDict[str, dict[str, Any]]
) -> dbc.Nav:
    """Create page links for navigation.

    `page_registry` page data is used to construct the navbar's page links. A page is
    included if it has a key `navbar` with a value of True set when the page was
    registered.

    Parameters
    ----------
    page_registry : OrderedDict[str, dict[str, Any]]
        Registry of app pages containing relevant page data.

    Returns
    -------
    dbc.Nav
        `Nav` container with a `NavLink` for each page.
    """
    return dbc.Nav(
        # Use list comprehension to create a NavLink for each page.
        [
            dbc.NavLink(
                page["name"], href=page["relative_path"], class_name="ps-3 pe-0 py-0"
            )
            for page in page_registry.values()
            if page.get("navbar")
        ],
        class_name="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    )


def create_navbar_component(
    page_registry: OrderedDict[str, dict[str, Any]]
) -> dbc.Navbar:
    """Create a navbar component with links to each page and branding.

    The navbar component contains 3 components wrapped within a container component. The
    three components are:
        1. brand_component: Branding for the project.
        2. dbc.NavbarToggler: toggle to show/hide page links when screen size is small.
        3. dbc.Collapse: Hides or shows content (in this case page links) with a
        vertical collapsing animation.

    Parameters
    ----------
    page_registry : OrderedDict[str, dict[str, Any]]
        Registry of app pages containing relevant page data.

    Returns
    -------
    dbc.Navbar
        `Navbar` component with page links and branding.
    """
    return dbc.Navbar(
        dbc.Container(
            [
                # Branding NavLink.
                brand_component,
                # Button to show/hide page links when screen size is small.
                dbc.NavbarToggler(id=NAVBAR_TOGGLER, n_clicks=0),
                # Add the page links to the collapse component. Visibility is controlled
                # via the `is_open` argument. When False, collapse component has no
                # effect, the `nav` created by `create_page_link_component()` is
                # displayed directly.
                dbc.Collapse(
                    create_page_link_component(page_registry),
                    id=NAVBAR_COLLAPSE,
                    is_open=False,
                    navbar=True,
                ),
            ],
            class_name="px-3",
            fluid=True,
        ),
        color="primary",
        dark=True,
    )


# The current state of the collapse component (open vs. closed), along with a click
# event of the toggler button, are used to change the state of the collapse component.
@callback(
    Output(NAVBAR_COLLAPSE, "is_open"),
    Input(NAVBAR_TOGGLER, "n_clicks"),
    State(NAVBAR_COLLAPSE, "is_open"),
)
def toggle_navbar_collapse(n_clicks: int, is_open: bool) -> bool:
    """Toggle the collapse to show/hide the navbar page links at small screen sizes.

    Parameters
    ----------
    n_clicks : int
        Number of clicks of the toggler.
    is_open : bool
        State of the navbar collapse component.

    Returns
    -------
    bool
        Updated `is_open` variable.
    """
    if n_clicks:
        return not is_open
    return is_open
