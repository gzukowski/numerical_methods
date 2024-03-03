from data import read_csv
from methods import macd, signal
import matplotlib.pyplot as plt



FILENAME = "BTC-DAILY.csv"


def main() -> None:
      dataset = read_csv(filename=FILENAME)

      dataset_display = dataset.tail(1000)

      macd_values = macd(dataset["close"])
      signal_values = signal(macd_values)

      print(len(signal_values), len(macd_values))

      #print(macd_values)

      plt.figure(figsize=(10, 6))
      plt.plot(dataset_display.index, macd_values, label='MACD', color='blue')
      plt.plot(dataset_display.index, signal_values, label='Signal Line', color='red')
      plt.plot(dataset_display.index, dataset_display["close"], label='BTC', color='yellow')

      plt.title('MACD and Signal Line')
      plt.xlabel('Date')
      plt.ylabel('Value')
      plt.legend()
      plt.grid(True)
      plt.show()
      #print(dataset)





if __name__ == "__main__":
      main()