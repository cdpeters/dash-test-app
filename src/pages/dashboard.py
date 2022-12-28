"""Layout for the dashboard page.

Arranges different dashboard elements on the dashboard page.

Variables:
    bar_chart_row
    hawaii_line_chart_row
    table_row
    layout
"""

from dash import html, register_page

from components.figures import avg_precip_line_chart, avg_temp_line_chart, bar_chart
from components.table import hawaii_climate_table

# Needed for the app to see this module as a page. The `navbar` argument is included so
# that this page will be added as a page link in the navbar.
register_page(__name__, navbar=True, icon_path="/assets/chart-line.svg")

# Create bar chart row.
bar_chart_row = html.Div(bar_chart)

# Create line chart row.
hawaii_line_chart_row = html.Div(
    [
        html.Div(avg_temp_line_chart),
        html.Div(avg_precip_line_chart),
    ],
)

# Create table row.
table_row = html.Div(
    html.Div(hawaii_climate_table),
)

# `layout` is required for Dash multi-page apps.
layout = html.Div(
    [
        html.Div(
            [
                html.H2("Dashboard"),
                html.P("This is the Dash Test App dashboard."),
            ],
            className="prose",
        ),
        bar_chart_row,
        hawaii_line_chart_row,
        table_row,
    ],
    className="p-4",
)
