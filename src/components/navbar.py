"""Build a navbar component with page links and branding.

The function `navbar` returns a Dash bootstrap components Navbar.
"""

import dash_bootstrap_components as dbc
from dash import html

from utils.constants import NAVBAR_COLLAPSE, NAVBAR_TOGGLER


def navbar(page_registry, brand_logo):
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
    # `nav` is a container that holds the page links.
    page_links = dbc.Nav(
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

    brand = dbc.Row(
        [
            # Brand logo.
            dbc.Col(html.Img(src=brand_logo, height="30px")),
            # App name.
            dbc.Col(dbc.NavbarBrand("Dash Test App", class_name="mx-2")),
        ],
        align="center",
        class_name="g-0",
    )

    return dbc.Navbar(
        dbc.Container(
            [
                # Branding NavLink
                dbc.NavLink(brand, href="/", class_name="ps-0"),
                # Button to show/hide collapse component with page links when screen
                # size is small.
                dbc.NavbarToggler(id=NAVBAR_TOGGLER, n_clicks=0),
                # Add `nav` to the collapse component. Visibility is controlled via the
                # `is_open` argument.
                dbc.Collapse(
                    page_links,
                    id=NAVBAR_COLLAPSE,
                    is_open=False,
                    navbar=True,
                ),
            ],
            class_name="dbc px-3",
            fluid=True,
        ),
    )
