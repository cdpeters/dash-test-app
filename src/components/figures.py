"""Create figures to be used on the dashboard page.

The module loads the figure template for the currently selected theme to be used as a
template in the figures that are created.

Current figures within this module:
    bar_chart : bar
"""

import plotly.express as px
from dash import dcc
from dash_bootstrap_templates import load_figure_template

from utils.constants import FIGURE_BAR, FIGURE_PRCP, FIGURE_TEMP, THEME

# Load figure template. Needed to apply the chosen bootstrap theme to figures.
load_figure_template(themes=THEME["name"])


def create_bar_chart(df):
    """Create bar chart from a DataFrame.

    Parameters
    ----------
    df : DataFrame
        Dataset containing data for the bar_chart.

    Returns
    -------
    Graph
        An instance of dcc.Graph containing a bar chart.

    """
    bar_chart = px.bar(
        data_frame=df,
        x="Fruit",
        y="Amount",
        color="City",
        barmode="group",
        template=THEME["name"],
    )

    return dcc.Graph(id=FIGURE_BAR, figure=bar_chart)


def create_hawaii_line_charts(df):
    """Create line charts from Hawaii climate data.

    Parameters
    ----------
    df : DataFrame
        Dataset containing climate data for the line charts.

    Returns
    -------
    Graph
        An instance of dcc.Graph containing a bar chart.

    """
    avg_temp_fig = px.line(
        data_frame=df,
        x="day",
        y="tobs",
        title="Average Daily Temperature in Hawaii",
        color="month",
        markers=True,
        labels={"day": "Day of month", "month": "Month", "tobs": "Temperature"},
        template=THEME["name"],
    )

    avg_prcp_fig = px.line(
        data_frame=df,
        x="day",
        y="prcp",
        title="Average Daily Precipitation in Hawaii",
        color="month",
        markers=True,
        labels={"day": "Day of month", "month": "Month", "prcp": "Precipitation"},
        template=THEME["name"],
    )

    return dcc.Graph(id=FIGURE_TEMP, figure=avg_temp_fig,), dcc.Graph(
        id=FIGURE_PRCP,
        figure=avg_prcp_fig,
    )
