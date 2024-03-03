import pandas as pd


BUY = 1
SELL = 0
INITIAL_BALANCE = 10000

def read_csv(filename : str) -> pd.DataFrame:
      return pd.read_csv(filename, usecols=["date", "close", "symbol"], nrows=1026).iloc[::-1].reset_index(drop=True)

      