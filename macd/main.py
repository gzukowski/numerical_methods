from data import read_csv
from methods import macd, signal
import matplotlib.pyplot as plt
import pandas as pd



FILENAME = "BTC-DAILY.csv"
INITIAL_BALANCE = 10000  # Initial balance for simulation
BUY = 1
SELL = 0




STOP_LOSS_THRESHOLD = 0.5  # 5% stop-loss threshold
GRACE_PERIOD = 5  # Number of time steps before applying stop-loss


def simulate_investment_better(intersection_points: list, dataset_display: pd.DataFrame) -> float:
      balance = INITIAL_BALANCE
      btc_balance = 0
      time_since_purchase = 0
      for point, macd_value, action in intersection_points:
            price = dataset_display["close"][point] 
            if action == BUY and macd_value > 0:  # Buy when MACD line crosses above signal line and MACD histogram is above zero
                  btc_balance = balance / price
                  balance = 0
                  time_since_purchase = 0
                  print(f"Buying {btc_balance} BTC at price {dataset_display.loc[point, 'close']} at time {point}")
            elif action == SELL:
                  if time_since_purchase >= GRACE_PERIOD and btc_balance > 0 and (price / btc_balance) < (1 - STOP_LOSS_THRESHOLD):
                        balance = btc_balance * price
                        btc_balance = 0
                        print(f"Selling all BTC at price {dataset_display.loc[point, 'close']} at time {point} due to stop-loss")
            time_since_purchase += 1
            print(f"{btc_balance:=}")

      print("end", btc_balance)
      if btc_balance > 0:  # Sell remaining BTC at the last data point
            print(btc_balance)
            balance = btc_balance * price
            print(f"Selling remaining {btc_balance} BTC at price {dataset_display.iloc[-1]['close']} at the last time point")
      return balance







def simulate_investment(intersection_points: list, dataset_display: pd.DataFrame) -> float:
      balance = INITIAL_BALANCE
      coins = 0

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

      final_balance = simulate_investment(intersection_points, dataset_display)

      print("---------------------")

      final_balance_better = simulate_investment_better(intersection_points, dataset_display)
      print("Final balance after simulation:", final_balance)
      print("Final balance after simulation2:", final_balance_better)

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

   



if __name__ == "__main__":
      main()

