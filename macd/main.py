from data import read_csv
from methods import macd, signal
import matplotlib.pyplot as plt
import pandas as pd



FILENAME = "BTC-DAILY.csv"
INITIAL_BALANCE = 10000  # Initial balance for simulation
BUY = 1
SELL = 0


def simulate_investment(intersection_points : list, dataset_display: pd.DataFrame) -> float:
      balance = INITIAL_BALANCE
      coins = 0

      for point in intersection_points:
            _, price, state = point
            coins_to_buy = balance / price
            if balance < 0:
                  return balance
            
            if state == BUY:
                  balance -= coins_to_buy * price
                  coins += coins_to_buy
            else:
                  balance += coins * price
                  coins = 0
      return balance
    



def main() -> None:

      dataset = read_csv(filename=FILENAME)

      dataset_display = dataset.tail(1000)

      macd_values = macd(dataset["close"])
      signal_values = signal(macd_values)


      plt.figure(figsize=(10, 6))
      plt.plot(dataset_display.index, macd_values, label='MACD', color='blue')
      plt.plot(dataset_display.index, signal_values, label='Signal Line', color='red')


      buy_points = []
      sell_points = []
      intersection_points = []
      for i in range(1, len(macd_values)):
            if macd_values[i] > signal_values[i] and macd_values[i - 1] <= signal_values[i - 1]:
                  buy_points.append((dataset_display.index[i], dataset_display["close"].iloc[i]))
                  intersection_points.append((dataset_display.index[i], macd_values[i], BUY))
            elif macd_values[i] < signal_values[i] and macd_values[i - 1] >= signal_values[i - 1]:
                  sell_points.append((dataset_display.index[i], dataset_display["close"].iloc[i]))
                  intersection_points.append((dataset_display.index[i], macd_values[i], SELL))

      for point in buy_points:
            plt.scatter(point[0], point[1], color='green', marker='^', s=50, zorder=3)

      for point in sell_points:
            plt.scatter(point[0], point[1], color='black', marker='v', s=50, zorder=3)

      for point, value, _ in intersection_points:
            plt.scatter(point, value, color='orange', marker='o', s=50, zorder=3)




      plt.plot(dataset_display.index, dataset_display["close"], label='BTC', color='yellow', zorder=2)
      plt.title('MACD and Signal Line')
      plt.xlabel('Date')
      plt.ylabel('Value')
      plt.legend()
      plt.grid(True)
      plt.show()


      final_balance = simulate_investment(intersection_points, dataset_display)
      print("Final balance after simulation:", final_balance)



if __name__ == "__main__":
      main()