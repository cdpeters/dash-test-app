"""Layout for the dashboard page."""

import dash_bootstrap_components as dbc
from dash import html, register_page

from components.figures import create_bar_chart, create_hawaii_line_charts
from components.table import create_table
from data.process_data import mean_jun_dec, sample_data

# Needed for the app to see this module as a page.
register_page(__name__, navbar=True)

# Create bar chart row.
bar_chart = dbc.Row(
    dbc.Col(
        create_bar_chart(df=sample_data),
        class_name="dbc",
        width=8,
    ),
    justify="center",
)

# Create line chart row.
avg_temp_fig, avg_prcp_fig = create_hawaii_line_charts(df=mean_jun_dec)
hawaii_line_charts = dbc.Row(
    [
        dbc.Col(
            avg_temp_fig,
            class_name="dbc",
            width=6,
        ),
        dbc.Col(
            avg_prcp_fig,
            class_name="dbc",
            width=6,
        ),
    ],
    justify="center",
)

# Create table row.
table = dbc.Row(
    dbc.Col(
        # Place a table.
        create_table(df=mean_jun_dec),
        width=10,
    ),
    justify="center",
)

# `layout` is required for Dash multi-page apps.
layout = dbc.Container(
    [
        html.H2("Dashboard", className="mt-3"),
        html.Hr(className="mt-2"),
        bar_chart,
        hawaii_line_charts,
        table,
    ],
    class_name="dbc px-3",
    fluid=True,
)
