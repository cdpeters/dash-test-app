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
from utils.constants import DASHBOARD_PAGE_ICON

# Needed for the app to see this module as a page. The `navbar` argument is included so
# that this page will be added as a page link in the navbar.
register_page(__name__, sidebar=True, icon_path=DASHBOARD_PAGE_ICON)

climate_table = html.Div(hawaii_climate_table, className="max-w-lg shadow-md")

# `layout` is required for Dash multi-page apps.
layout = html.Div(
    [
        html.Div(
            "Dashboard",
            className="""py-1.5 flex justify-center bg-slate-700 text-emerald-50
            font-semibold""",
        ),
        html.Div(
            [
                html.P(
                    "This is the Dash Test App dashboard.",
                    className="mb-4 text-inherit",
                ),
                html.Div(
                    [
                        bar_chart,
                        html.Br(),
                        avg_temp_line_chart,
                        html.Br(),
                        avg_precip_line_chart,
                        html.Br(),
                        climate_table,
                    ],
                    className="pb-6 text-inherit",
                ),
            ],
            className="p-4 text-slate-700",
        ),
    ],
    className="min-h-screen",
)
