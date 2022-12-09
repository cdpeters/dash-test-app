"""Build a navbar component with page links and branding.

The function `navbar` returns a Dash bootstrap components Navbar.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html

from utils.constants import NAVBAR_COLLAPSE, NAVBAR_TOGGLER

if TYPE_CHECKING:
    from collections import OrderedDict


def create_navbar_component(page_registry: OrderedDict, brand_logo: str) -> dbc.Navbar:
    """Create a navbar component with links to each page and branding.

    `page_registry` page data is used to construct NavLink components to link to the
    different app pages. These NavLink components are then assembled into a Navbar
    component that includes a `brand_logo` and a NavBrand component.

    Parameters
    ----------
    page_registry : OrderedDict
        Registry of app pages to be used to construct page links on the navbar.
    brand_logo : str
        Path to the brand logo used in the navbar.

    Returns
    -------
    Navbar
        Navbar component with page links.

    """
    return dbc.Navbar(
        dbc.Container(
            [
                # Branding NavLink
                dbc.NavLink(
                    create_brand_component(brand_logo), href="/", class_name="ps-0"
                ),
                # Button to show/hide collapse component with page links when screen
                # size is small.
                dbc.NavbarToggler(id=NAVBAR_TOGGLER, n_clicks=0),
                # Add `nav` to the collapse component. Visibility is controlled via the
                # `is_open` argument.
                dbc.Collapse(
                    create_page_link_component(page_registry),
                    id=NAVBAR_COLLAPSE,
                    is_open=False,
                    navbar=True,
                ),
            ],
            class_name="dbc px-3",
            fluid=True,
        ),
    )


def create_page_link_component(page_registry: OrderedDict) -> dbc.Nav:
    """Create page links for navigation.

    Parameters
    ----------
    page_registry : OrderedDict
        Registry of app pages to be used to construct page links on the navbar.

    Returns
    -------
    dbc.Nav
        Nav container with a NavLink for each page.
    """
    # `Nav` is a container that holds the page links.
    return dbc.Nav(
        # Use list comprehension to create a NavLink for each page.
        [
            dbc.NavLink(
                page["name"],
                href=page["relative_path"],
                class_name="ps-3 pe-0",
            )
            for page in page_registry.values()
            if page.get("navbar")
        ],
        class_name="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    )


def create_brand_component(brand_logo: str) -> dbc.Row:
    """Create branding for a navbar.

    Parameters
    ----------
    brand_logo : str
        Path to the brand logo used in the navbar.

    Returns
    -------
    dbc.Row
        Row component containing the branding name and logo.
    """
    return dbc.Row(
        [
            # Brand logo.
            dbc.Col(html.Img(src=brand_logo, height="30px")),
            # App name.
            dbc.Col(dbc.NavbarBrand("Dash Test App", class_name="mx-2")),
        ],
        align="center",
        class_name="g-0",
    )


# A callback for toggling the collapsible menu of page links when the screen size is
# small.
@callback(
    Output(NAVBAR_COLLAPSE, "is_open"),
    Input(NAVBAR_TOGGLER, "n_clicks"),
    State(NAVBAR_COLLAPSE, "is_open"),
)
def toggle_navbar_collapse(n_clicks: int, is_open: bool) -> bool:
    """Toggle the collapse of the navbar page links dropdown at small screen sizes.

    Parameters
    ----------
    n_clicks : int
        Number of clicks of the toggler.
    is_open : bool
        State of the navbar collapse component.

    Returns
    -------
    bool
        Update of the `is_open` variable.
    """
    if n_clicks:
        return not is_open
    return is_open
