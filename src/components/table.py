"""Creates Dash DataTables for any page of the app."""

from dash import dash_table

from utils.constants import TABLE


def create_table(df):
    """Return a Div containing a DataTable built from the columns of a DataFrame.

    Parameters
    ----------
    df : DataFrame
        Dataset containing data for the table.

    Returns
    -------
    Div
        An instance of html.Div containing an instance of DataTable.

    """
    return dash_table.DataTable(
        # `orient` sets the format of the output of `to_dict()`.
        # `"records"` makes that output a list of dictionaries.
        id=TABLE,
        data=df.to_dict(orient="records"),
        columns=[{"name": col, "id": col} for col in df.columns],
        style_as_list_view=True,
        style_header={"fontWeight": "bold"},
    )
