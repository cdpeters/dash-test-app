"""Load data resources."""

from pathlib import Path

import ibis
import pandas as pd


def load_data(data_dir):
    """Load data resources into appropriate data structures.

    Parameters
    ----------
    data_dir : str
        Path to the project's data directory.

    Returns
    -------
    tuple
        Contains DataFrames created from the data resources.

    """
    # Load NBA playoff team data from 1996-97 to 2021-22.
    playoff_teams = pd.read_csv(data_dir / "playoff_teams_df.csv")
    # Load Hawaii weather measurements and station data.
    measurement, station = load_hawaii_weather(path=data_dir / "hawaii.sqlite")

    return playoff_teams, measurement, station


def load_hawaii_weather(path):
    """Read sqlite db of Hawaii weather data.

    Parameters
    ----------
    path : str
        Path to sqlite db.

    Returns
    -------
    tuple
        Contains DataFrames of measurement and station data.

    """
    # Connect to the db
    db = ibis.sqlite.connect(path)

    tables = db.list_tables()
    # measurement and station are ibis Table instances.
    measurement = db.table(name=tables[0])
    station = db.table(name=tables[1])

    # Execute creates DataFrames from the Tables.
    return measurement.execute(), station.execute()


# Load Data ----------------------------------------------------------------------------
# Uses the file path (`__file__`) of this module to form the data directory path.
# parents[2] removes 3 pieces (since index 2 is 3rd element) from the path: file name,
# and two parent directories.
data_dir = Path(__file__).parents[2] / "data"
playoff_teams, measurement, station = load_data(data_dir=data_dir)

# Sample data from plotly.
sample_data = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
