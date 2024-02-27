import numpy as np
import pandas as pd



def calc_alpha(periods : int) -> int:
      return 2 / (periods + 1)

def ema(periods : int, dataset : pd.DataFrame) -> float:
      #ema_values = []

      alpha = calc_alpha(periods)

      denominator = sum((1 - alpha) ** i for i in range(periods + 1))

      numerator = sum((1 - alpha) ** i * dataset["close"][i] for i in range(periods + 1))

      return numerator / denominator
      

def macd(dataset : pd.DataFrame):
      print(ema(26, dataset))
      print(ema(12, dataset))