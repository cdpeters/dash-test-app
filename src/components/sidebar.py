"""Build a sidebar component with page links.

Sidebar creation function takes in the page registry and builds page links that are
placed within a `Nav` component. The `Nav` component represents the sidebar.

Functions:
    create_sidebar_component
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import dash_bootstrap_components as dbc
from dash import html

if TYPE_CHECKING:
    from collections import OrderedDict


def create_sidebar_component(
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
    page_links = [
        dbc.NavLink(
            page["name"], href=page["relative_path"], active="exact", class_name="py-1"
        )
        for page in page_registry.values()
        if page.get("navbar")
    ]

    heading = html.Div(
        [
            html.Div(
                "Navigation",
                className="ps-2 mb-1 mt-3",
                style={"color": "white", "fontSize": 13, "fontWeight": "bold"},
            ),
            html.Hr(className="mt-1 mb-0", style={"color": "var(--bs-gray-300"}),
        ],
        className="px-2",
    )

    return dbc.Nav(
        # `page_links`` has to be unpacked since it is a list (the `children` argument
        # list must not contain a list).
        [
            heading,
            *page_links,
        ],
        class_name="flex-nowrap",
        vertical=True,
        pills=True,
    )
