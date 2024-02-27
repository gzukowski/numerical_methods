import pandas as pd


def read_csv(filename : str) -> pd.DataFrame:
      return pd.read_csv(filename, usecols=["date", "close", "symbol"], nrows=1000)
      