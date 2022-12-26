"""Create figures to be used on the dashboard page.

Loads the figure template for the currently selected theme setting it as the default
template for figure creation. Graph components are created containing different charts.

Variables:
    bar_chart
    avg_temp_line_chart
    avg_precip_line_chart
"""

import plotly.express as px
from dash import dcc

from data.process_data import sample_data, transformed_measurement
from utils.constants import FIGURE_BAR, FIGURE_PRECIP, FIGURE_TEMP

# Create `Graph` component containing a bar chart from `sample_data`.
bar_chart = dcc.Graph(
    id=FIGURE_BAR,
    figure=px.bar(
        data_frame=sample_data,
        x="Fruit",
        y="Amount",
        color="City",
        barmode="group",
        height=350,
    ),
    config={
        "displayModeBar": False,
    },
)

# Create `Graph` component containing average temperature data from Hawaii.
avg_temp_line_chart = dcc.Graph(
    id=FIGURE_TEMP,
    figure=px.line(
        data_frame=transformed_measurement,
        x="Day",
        y="Temperature",
        title="Average Daily Temperature in Hawaii",
        color="Month",
        markers=True,
        labels={"Day": "Day of month"},
        height=350,
    ),
    config={
        "displayModeBar": False,
    },
)

# Create `Graph` component containing average precipitation data from Hawaii.
avg_precip_line_chart = dcc.Graph(
    id=FIGURE_PRECIP,
    figure=px.line(
        data_frame=transformed_measurement,
        x="Day",
        y="Precipitation",
        title="Average Daily Precipitation in Hawaii",
        color="Month",
        markers=True,
        labels={"Day": "Day of month"},
        height=350,
    ),
    config={
        "displayModeBar": False,
    },
)


# def create_graph_component(
#     plotting_func: Callable[..., go.Figure], id: str, fig_params: dict
# ) -> dcc.Graph:
#     """Create a graph component for any plotly express figure type.

#     Parameters
#     ----------
#     plotting_func : Callable[..., go.Figure]
#         Plotly express plotting function.
#     id : str
#         Id for the Graph component
#     fig_params : dict
#         Parameters to create and style the figure.

#     Returns
#     -------
#     dcc.Graph
#         Graph object containing the figure.
#     """
#     figure = plotting_func(**fig_params)

#     return Graph(id=id, figure=figure)
