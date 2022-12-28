"""Build a sidebar component with page links.

Sidebar creation function takes in the page registry and builds page links that are
placed within a `Nav` component. The `Nav` component represents the sidebar.

Functions:
    create_sidebar_component
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from dash import html

from utils.constants import DATA_COLLAB_LOGO

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
            [
                html.Img(src=page["icon_path"], className="aspect-auto h-3"),
                html.Div(
                    page["name"], className="font-semibold text-inherit bg-inherit"
                ),
            ],
            href=page["relative_path"],
            className="""px-4 py-2 flex space-x-2 items-center text-emerald-50
            hover:bg-slate-700 active:bg-emerald-50 active:text-slate-800
            focus:bg-emerald-50 focus:text-slate-800""",
        )
        for page in page_registry.values()
        if page.get("navbar")
    ]

    heading = html.A(
        [
            html.Img(src=DATA_COLLAB_LOGO, className="aspect-square h-5"),
            html.Div("Dash Test App", className="font-semibold text-emerald-50"),
        ],
        href="/",
        className="px-1.5 py-2 flex space-x-1.5 items-center",
    )

    return html.Div(
        # `page_links`` has to be unpacked since it is a list (the `children` argument
        # list must not contain a list).
        [
            heading,
            *page_links,
        ],
    )
