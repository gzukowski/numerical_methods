import numpy as np
import pandas as pd



def ema(periods : int, dataset : pd.DataFrame, start: int) -> float:

      start = start - periods

      alpha = 2 / (periods + 1)

      denominator = sum((1 - alpha) ** i for i in range(periods))

      numerator = sum((1 - alpha) ** i * dataset[i+start] for i in range(periods))

      return numerator / denominator
      


def signal(macd_values : list[float]):
      signal_values = []

      for day in range(0, 1000):

            if day < 9:
                  signal_values.append(0)
                  continue

            signal_values.append(ema(9, macd_values, day))

      return signal_values

def macd(dataset : pd.DataFrame) -> list[float]:

      macd_values = []

      for day in range(26, 1026):
            macd_values.append(ema(12, dataset, day) - ema(26, dataset, day))

      return macd_values