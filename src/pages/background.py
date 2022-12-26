"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""

from dash import dcc, html, register_page

register_page(__name__, navbar=True)

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
    """
)

layout = html.Div(
    [
        html.H2("Project Background"),
        html.Hr(),
        html.Div(
            """
            This app will serve as a testing ground for dashboard development.
            The intention is to use it as boilerplate for creating dashboards in
            future projects.
        """
        ),
        html.Br(),
        markdown,
        html.Br(),
    ],
)
