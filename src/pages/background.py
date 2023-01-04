"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""

from dash import dcc, html, register_page

from utils.constants import BACKGROUND_PAGE_ICON

register_page(__name__, sidebar=True, icon_path=BACKGROUND_PAGE_ICON)

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
                html.Div(markdown),
            ],
            className="py-4 prose prose-slate max-w-2xl mx-auto",
        ),
    ],
    className="min-h-screen",
)
