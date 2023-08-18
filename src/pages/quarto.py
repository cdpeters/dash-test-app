"""Layout for the quarto example page.

Displays an example of a Quarto html document being rendered in an iframe.

Variables:
    quarto
    layout
"""

from dash import html, register_page

from utils.constants import (
    BACKGROUND_ICON_DARK,
    BACKGROUND_ICON_LIGHT,
    ID_QUARTO_ICON,
    ID_QUARTO_LINK,
)

register_page(
    __name__,
    sidebar=True,
    order=3,
    id_icon=ID_QUARTO_ICON,
    id_link=ID_QUARTO_LINK,
    icon_light=BACKGROUND_ICON_LIGHT,
    icon_dark=BACKGROUND_ICON_DARK,
)

quarto = html.Iframe(
    src="/assets/html/quarto_practice.html", width="671px", className="h-96"
)

layout = html.Div(
    [
        html.Div(
            "Quarto Example",
            className="""py-1.5 flex justify-center bg-slate-700 text-emerald-50
            font-semibold""",
        ),
        html.Div(
            quarto,
            className="py-4 mb-8 max-w-2xl mx-auto",
        ),
    ],
    className="min-h-screen",
)
