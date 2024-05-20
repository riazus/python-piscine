import os
import pandas as pd


def load(path: str):
    """
    Loads a CSV file from the specified path and returns
    the first 5 rows of the DataFrame as a string.
    """
    if not os.path.exists(path) \
            or not os.path.isfile(path) \
            or not path.endswith(".csv"):
        return None

    try:
        return pd.read_csv(path)
    except Exception:
        return None
