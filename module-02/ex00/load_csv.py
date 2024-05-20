import os
import pandas as pd


def load(path: str):
    if not os.path.exists(path) or not os.path.isfile(path):
        return None

    try:
        table = pd.read_csv(path)
        dimension = f"{table.shape[0]}, {table.shape[1]}"
        header = f"Loading dataset of dimension ({dimension})\n"
        return header + table.head(5).to_string()
    except Exception:
        return None
