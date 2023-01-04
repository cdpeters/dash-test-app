"""Build a footer component with a link to the app source code on github.

Variables:
    footer_component
"""

from dash import dcc, html

from utils.constants import APP_SOURCE_CODE_URL, DATA_COLLAB_LOGO, GITHUB_ICON

footer_component = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.Img(src=DATA_COLLAB_LOGO, className="aspect-square h-4"),
                    html.Div("Data Collab", className="text-emerald-50"),
                ],
                className="px-3 flex space-x-1.5 items-center",
            ),
            dcc.Link(
                [
                    html.Img(src=GITHUB_ICON, className="aspect-square h-4"),
                    html.Div("Source Code", className="text-emerald-50"),
                ],
                href=APP_SOURCE_CODE_URL,
                refresh=True,
                target="_blank",
                className="px-3 flex space-x-1.5 items-center",
            ),
        ],
        className="py-1.5 bg-slate-700 flex items-center justify-between text-sm",
    ),
    className="fixed left-32 bottom-0 right-0",
)
