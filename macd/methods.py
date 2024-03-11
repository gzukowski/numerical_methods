import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



BUY = 1
SELL = 0
INITIAL_BALANCE = 10000



def display_chart(macd_values: list[float],
                  signal_values: list[float],
                  dataset: pd.DataFrame,
                  buy_points: list,
                  sell_points: list,
                  intersection_points: list,
                  label: str,
                  rng : int = None) -> None:
      

      plt.figure(figsize=(10, 6))
      plt.plot(dataset.index[:rng], macd_values[:rng], label='MACD', color='blue')
      plt.plot(dataset.index[:rng], signal_values[:rng], label='Signal Line', color='red')

      for point in buy_points:
            plt.scatter(point[0], point[1], color='green', marker='^', s=50, zorder=3)

      for point in sell_points:
            plt.scatter(point[0], point[1], color='black', marker='v', s=50, zorder=3)

      for point, value, _ in intersection_points:
            plt.scatter(point, value, color='orange', marker='o', s=50, zorder=3)


      plt.plot(dataset.index[:rng], dataset["close"][:rng], label=label, color='yellow', zorder=2)
      plt.title('MACD and Signal Line')
      plt.xlabel('Day')
      plt.ylabel('Value')
      plt.legend()
      plt.grid(True)
      plt.show()


def analyze_macd(macd_values : list[float], signal_values : list[float], dataset : pd.DataFrame, divisor : int = 1 ):
      buy_points = []
      sell_points = []
      intersection_points = []
      for i in range(1, len(macd_values)//divisor):
            if macd_values[i] > signal_values[i] and macd_values[i - 1] <= signal_values[i - 1]:
                  buy_points.append((dataset.index[i], dataset["close"].iloc[i]))
                  intersection_points.append((dataset.index[i], macd_values[i], BUY))
            elif macd_values[i] < signal_values[i] and macd_values[i - 1] >= signal_values[i - 1]:
                  sell_points.append((dataset.index[i], dataset["close"].iloc[i]))
                  intersection_points.append((dataset.index[i], macd_values[i], SELL))


      return buy_points, sell_points, intersection_points


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



INITIAL_BALANCE = 0
INITIAL_COINS = 1000
RSI_PERIOD = 14
BUY = 1
SELL = 0





def calculate_rsi(prices):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=RSI_PERIOD).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=RSI_PERIOD).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def simulate_investment_rsi(intersection_points: list, dataset_display: pd.DataFrame) -> float:
      balance = 0
      coins = INITIAL_COINS
      price = dataset_display["close"][26]
      print(f"Starting with rsi with balance: {coins * price}")

      rsi_values = calculate_rsi(dataset_display["close"])

      for point in intersection_points:
            index, _, state = point
            price = dataset_display["close"][index]
            rsi = rsi_values[index]

            if state == BUY and rsi < 30:  # oversold
                  coins_to_buy = balance / price
                  balance -= coins_to_buy * price
                  coins += coins_to_buy
                  #print(f"Buying {coins_to_buy:.8f} coins at ${price:.2f} each. Balance: ${balance:.2f}")
            elif state == SELL and rsi > 70:  # overbought
                  balance += coins * price
                  #print(f"Selling {coins:.8f} coins at ${price:.2f} each. Balance: ${balance:.2f}")
                  coins = 0

      if coins > 0:
            balance += coins * dataset_display["close"].iloc[-1]
            #print(f"Selling remaining {coins:.8f} coins at ${dataset_display['close'].iloc[-1]:.2f} each. Balance: ${balance:.2f}")

      return balance


def simulate_investment(intersection_points: list, dataset_display: pd.DataFrame) -> float:
      balance = 0
      coins = INITIAL_COINS
      price = dataset_display["close"][26]
      print(f"Starting simple with balance: {coins * price}")

      for point in intersection_points:
            index, _, state = point
            price = dataset_display["close"][index]

            if state == BUY:
                  coins_to_buy = balance / price
                  balance -= coins_to_buy * price
                  coins += coins_to_buy
                  print(f"Buying {coins_to_buy:.8f} coins at ${price:.2f} each. Balance: ${balance:.2f}")
            elif state == SELL:
                  balance += coins * price
                  print(f"Selling {coins:.8f} coins at ${price:.2f} each. Balance: ${balance:.2f}")
                  coins = 0

      if coins > 0:
            balance += coins * dataset_display["close"].iloc[-1]
            print(f"Selling remaining {coins:.8f} coins at ${dataset_display['close'].iloc[-1]:.2f} each. Balance: ${balance:.2f}")

      return balance

