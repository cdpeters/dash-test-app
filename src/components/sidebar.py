"""Build a sidebar component with page links.

Sidebar creation function takes in the page registry and builds page links that are
placed within a `Nav` component. The `Nav` component represents the sidebar.

Functions:
    create_sidebar_component
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from dash import html

if TYPE_CHECKING:
    from collections import OrderedDict


def create_sidebar_component(
    page_registry: OrderedDict[str, dict[str, Any]]
) -> html.Div:
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
    html.Div
        `A navbar with a link to each page.
    """
    page_links = [
        html.A(
            page["name"], href=page["relative_path"], className="px-4 hover:bg-pink-500"
        )
        for page in page_registry.values()
        if page.get("navbar")
    ]

    heading = html.Div(
        [
            html.Div("Navigation", className="bg-purple-400"),
            html.Hr(),
        ],
    )

    return html.Div(
        # `page_links`` has to be unpacked since it is a list (the `children` argument
        # list must not contain a list).
        [
            heading,
            *page_links,
        ],
    )
