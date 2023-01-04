"""Creates Dash DataTable from a DataFrame.

Variables:
    hawaii_climate_table
"""

from dash.dash_table import DataTable
from dash.dash_table.Format import Format, Scheme

from data.process_data import transformed_measurement
from utils.constants import TABLE_CLIMATE

hawaii_climate_table = DataTable(
    id=TABLE_CLIMATE,
    data=transformed_measurement.to_dict(orient="records"),
    # Each column requires at least `name` and `id`. `name` is the string that will be
    # used as the column header. `id` is the name of the column from the DataFrame from
    # which to take the data from.
    columns=[
        {
            "name": "Month",
            "id": "Month",
        },
        {
            "name": "Day",
            "id": "Day",
        },
        {
            "name": "Precipitation",
            "id": "Precipitation",
            "type": "numeric",
            "format": Format(precision=2, scheme=Scheme.fixed),
        },
        {
            "name": "Temperature",
            "id": "Temperature",
            "type": "numeric",
            "format": Format(precision=1, scheme=Scheme.fixed),
        },
    ],
    style_as_list_view=True,
    style_header={
        "color": "#ecfdf5",
        "fontWeight": "bold",
        "backgroundColor": "#475569",
    },
    style_cell_conditional=[
        {"if": {"column_id": col}, "textAlign": "left"} for col in ["Month"]
    ],
    style_cell={"padding": "10px"},
    style_data={"border": "none"},
    style_data_conditional=[
        {"if": {"row_index": "odd"}, "backgroundColor": "#f1f5f9"},
        {"if": {"row_index": "even"}, "backgroundColor": "#f8fafc"},
    ],
)
