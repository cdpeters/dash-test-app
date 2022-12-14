"""Data processing prior to figure or table creation.

Transformations are applied to the relevant DataFrames to prepare them for usage in
figures and/or tables.

Variables:
    transformed_measurement
    sample_data
Functions:
    transform_measurement
"""

import pandas as pd
from pandas import DataFrame

from data.load_data import hawaii_weather_data

# Set the `measurement` DataFrame from the Hawaii data dictionary.
measurement = hawaii_weather_data["measurement"]


def transform_measurement(input_df: DataFrame) -> DataFrame:
    """Transform the input DataFrame for use in figures and tables.

    Month and day of the month columns are created from the `date` column. Data is
    filtered to June and December only. Data is then grouped by levels `month` and
    `day`. The mean is calculated for each day across all years. The dataset is
    restacked in a logical order (June observations before December) and the columns
    renamed.

    Parameters
    ----------
    input_df : DataFrame
        Dataset of Hawaii temperature and precipitation observations.

    Returns
    -------
    DataFrame
        Transformed dataset ready for figure and table creation.
    """
    # Extract month and day of month data from `date` column.
    df = input_df.copy()
    df["month"] = pd.DatetimeIndex(df["date"]).month_name()
    df["day"] = pd.DatetimeIndex(df["date"]).day
    df.drop(["id", "station", "date"], axis=1, inplace=True)

    # Filter for June and December data.
    df_jun_dec = df.loc[(df["month"] == "June") | (df["month"] == "December")]

    # Replace month name with abbreviation.
    df_jun_dec = df_jun_dec.replace({"month": {"June": "Jun", "December": "Dec"}})

    # Group by month and day of month, calculate mean.
    df_jun_dec_avg = df_jun_dec.groupby(["month", "day"], as_index=False)[
        ["prcp", "tobs"]
    ].mean()

    # Stack June data above December data.
    df_jun_dec_avg = df_jun_dec_avg.sort_values(
        by=["month", "day"], ascending=[False, True]
    )

    # Rename each column as titles.
    transformed_df = df_jun_dec_avg.rename(
        columns={
            "month": "Month",
            "day": "Day",
            "prcp": "Precipitation",
            "tobs": "Temperature",
        }
    )

    return transformed_df


transformed_measurement = transform_measurement(measurement)

# Sample data from plotly.
sample_data = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
