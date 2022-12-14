"""Load data resources.

Loads data into DataFrames for further processing and for the production of example
figures and tables.

Variables:
    hawaii_weather_data
    playoff_teams
Functions:
    load_sqlite_data
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import ibis
import pandas as pd
from pandas import DataFrame

from utils.constants import DATA_DIR, GOOGLE_DRIVE_DIR

if TYPE_CHECKING:
    from pathlib import Path


def load_sqlite_data(path: Path) -> dict[str, DataFrame]:
    """Read sqlite database and return a dict of DataFrames.

    Returns all tables within a sqlite database as DataFrames without any processing.

    Parameters
    ----------
    path : Path
        pathlib Path to sqlite db.

    Returns
    -------
    dict[str, DataFrame]
        Keys are the table names and values are the associated DataFrames.
    """
    # Connect to the db.
    db = ibis.sqlite.connect(path)
    # Collect table names.
    tables_names = db.list_tables()
    # `db.table()` returns an ibis `Table` instance and `execute()` converts it into a
    # DataFrame.
    return {name: db.table(name=name).execute() for name in tables_names}


hawaii_weather_data = load_sqlite_data(path=GOOGLE_DRIVE_DIR / "hawaii.sqlite")
playoff_teams = pd.read_csv(DATA_DIR / "playoff_teams_df.csv")
