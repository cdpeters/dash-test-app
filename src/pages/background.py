"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""

from dash import dcc, html, register_page

from utils.constants import (
    BACKGROUND_ICON_DARK,
    BACKGROUND_ICON_LIGHT,
    ID_BACKGROUND_ICON,
    ID_BACKGROUND_LINK,
)

register_page(
    __name__,
    sidebar=True,
    order=1,
    id_icon=ID_BACKGROUND_ICON,
    id_link=ID_BACKGROUND_LINK,
    icon_light=BACKGROUND_ICON_LIGHT,
    icon_dark=BACKGROUND_ICON_DARK,
)

markdown = dcc.Markdown(
    """
    #### Markdown Element

    - This is a markdown element in Dash. All normal markdown features
    should work such as code snippets:
    ```python
    import pandas as pd

    df = pd.DataFrame(
        {
            "col1": ["value1", "value2", "value3"],
            "col2": [1, 3, 9],
            "col3": [0.4, 2.6, -1.2]
        }
    )
    ```

    #### Additional Example Section
    1. Item 1 in a numbered list
        - This item has an unordered list
        - The unordered list has 2 items in it
    1. Item 2 in a numbered list


    > Note. This is a link to the home page of the [*Dash Test App*](/)

    This concludes the markdown example. Any experiments with markdown syntax can be
    done on this page to see the output on the website.
    """,
)

layout = html.Div(
    [
        html.Div(
            "Project Background",
            className="""py-1.5 flex justify-center bg-slate-700 text-emerald-50
            font-semibold""",
        ),
        html.Div(
            [
                html.P(
                    """This app will serve as a testing ground for dashboard
                    development. The intention is to use it as boilerplate for creating
                    dashboards in future projects."""
                ),
                markdown,
            ],
            className="py-4 mb-8 prose prose-slate max-w-2xl mx-auto",
        ),
    ],
    className="min-h-screen",
)
