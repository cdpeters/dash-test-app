"""Build a sidebar component with page links.

The create sidebar function takes in the page registry and builds page links. There is
also a header that redirects to the home page of the app.

Functions:
    create_sidebar_component
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from dash import dcc, html

if TYPE_CHECKING:
    from collections import OrderedDict


def create_sidebar_component(
    page_registry: OrderedDict[str, dict[str, Any]]
) -> html.Div:
    """Create the sidebar component with page links for navigation.

    `page_registry` page data is used to construct the sidebar's page links. A page is
    included if it has a `sidebar` key with a value of True set when the page was
    registered.

    Parameters
    ----------
    page_registry : OrderedDict[str, dict[str, Any]]
        Registry of app pages containing relevant page data.

    Returns
    -------
    html.Div
        A sidebar with a link to each page.
    """
    page_links = [
        dcc.Link(
            [
                html.Img(src=page["icon_path"], className="aspect-square w-3"),
                html.Div(page["name"], className="text-sm text-inherit bg-inherit"),
            ],
            href=page["relative_path"],
            className="""px-4 py-2 flex space-x-2 items-center text-emerald-50
            hover:bg-slate-700 active:bg-emerald-50 active:text-slate-800
            focus:bg-emerald-50 focus:text-slate-800""",
        )
        for page in page_registry.values()
        if page.get("sidebar")
    ]

    heading = dcc.Link(
        [
            html.Div(
                "Dash Test App",
                className="py-3 text-center font-semibold text-emerald-50",
            ),
        ],
        href="/",
    )

    return html.Div(
        # `page_links` has to be unpacked since it is a list (i.e. the `children`
        # argument can be a list but it must not contain a list as an element).
        [
            heading,
            *page_links,
        ],
        className="bg-slate-800 h-screen w-32 w- fixed overflow-auto",
    )
