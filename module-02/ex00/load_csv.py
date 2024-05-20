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
        table = pd.read_csv(path)
        dimension = f"{table.shape[0]}, {table.shape[1]}"
        header = f"Loading dataset of dimension ({dimension})\n"
        return header + table.head(5).to_string()
    except Exception:
        return None
