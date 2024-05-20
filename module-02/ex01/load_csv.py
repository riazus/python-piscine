import os
import pandas as pd


def load(path: str):
    if not os.path.exists(path) or not os.path.isfile(path):
        return None

    try:
        return pd.read_csv(path)
    except Exception:
        return None
