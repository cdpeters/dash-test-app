"""Data processing prior to figure or table creation."""

import pandas as pd

from data.load_data import measurement

# Extract the month and day from the date column.
measurement["month"] = pd.DatetimeIndex(data=measurement["date"]).month_name()
measurement["day"] = pd.DatetimeIndex(data=measurement["date"]).day
measurement.drop(labels="date", axis=1, inplace=True)

# Filter the DataFrame by June and December.
meas_jun = measurement[(measurement["month"] == "June")]
meas_dec = measurement[(measurement["month"] == "December")]

# Group by day of the month and calculate the mean across all years for that day of the
# month.
mean_jun = meas_jun.groupby(by="day")[["prcp", "tobs"]].mean()
mean_dec = meas_dec.groupby(by="day")[["prcp", "tobs"]].mean()

mean_jun["month"] = "Jun"
mean_dec["month"] = "Dec"

# Reset index so that the day of the month is a column that can be plotted.
mean_jun = mean_jun.reset_index()
mean_dec = mean_dec.reset_index()

# Stack the results from the two DataFrames.
mean_jun_dec = pd.concat(objs=[mean_jun, mean_dec], ignore_index=True)

# mean_jun.join(other=mean_dec, how="right", lsuffix="_jun", rsuffix="_dec")

# Sample data from plotly.
sample_data = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
