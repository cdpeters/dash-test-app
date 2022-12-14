"""Layout for the dashboard page.

Arranges different dashboard elements on the dashboard page.

Variables:
    bar_chart_row
    hawaii_line_chart_row
    table_row
    layout
"""

import dash_bootstrap_components as dbc
from dash import html, register_page

from components.figures import avg_precip_line_chart, avg_temp_line_chart, bar_chart
from components.table import hawaii_climate_table

# Needed for the app to see this module as a page. The `navbar` argument is included so
# that this page will be added as a page link in the navbar.
register_page(__name__, navbar=True)

# Create bar chart row.
bar_chart_row = dbc.Row(
    dbc.Col(bar_chart, width=8),
    justify="center",
    class_name="my-3",
)

# Create line chart row.
hawaii_line_chart_row = dbc.Row(
    [
        dbc.Col(avg_temp_line_chart, width=6),
        dbc.Col(avg_precip_line_chart, width=6),
    ],
    justify="center",
    class_name="my-3",
)

# Create table row.
table_row = dbc.Row(
    dbc.Col(hawaii_climate_table, width=10),
    justify="center",
    class_name="my-3",
)

# `layout` is required for Dash multi-page apps.
layout = dbc.Container(
    [
        html.H2("Dashboard", className="mt-3"),
        html.Hr(className="mt-2"),
        bar_chart_row,
        hawaii_line_chart_row,
        table_row,
    ],
    class_name="px-3",
    fluid=True,
)
