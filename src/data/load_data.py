"""Load data resources."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

import ibis
import pandas as pd
from ibis.expr.types.relations import Table

from utils.constants import DATA_DIR, GOOGLE_DRIVE_DIR

if TYPE_CHECKING:
    from pathlib import Path

DataFrames: TypeAlias = tuple[pd.DataFrame, ...]


def load_data(data_dir: Path, google_drive_dir: Path) -> DataFrames:
    """Load data resources into appropriate data structures.

    Parameters
    ----------
    data_dir : Path
        pathlib Path to the project's data directory.
    google_drive_dir : Path
        pathlib Path to a shared google drive collaboration directory.

    Returns
    -------
    tuple
        Contains DataFrames created from the data resources.

    """
    # Load NBA playoff team data from 1996-97 to 2021-22.
    playoff_teams = pd.read_csv(data_dir / "playoff_teams_df.csv")
    # Load Hawaii weather measurements and station data.
    measurement, station = load_hawaii_weather(path=google_drive_dir / "hawaii.sqlite")

    return playoff_teams, measurement, station


def load_hawaii_weather(path: Path) -> DataFrames:
    """Read sqlite db of Hawaii weather data.

    Parameters
    ----------
    path : Path
        pathlib Path to sqlite db.

    Returns
    -------
    tuple
        Contains DataFrames of measurement and station data.
    """
    # Connect to the db
    db = ibis.sqlite.connect(path)
    tables = db.list_tables()
    # measurement and station are ibis Table instances.
    measurement: Table = db.table(name=tables[0])
    # print("from load_data.py, load_hawaii_weather function:", type(measurement))
    station: Table = db.table(name=tables[1])

    # `execute()` creates DataFrames from the Tables.
    return measurement.execute(), station.execute()


# Load Data ----------------------------------------------------------------------------
playoff_teams, measurement, station = load_data(
    data_dir=DATA_DIR,
    google_drive_dir=GOOGLE_DRIVE_DIR,
)
