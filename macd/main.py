from data import read_csv
from methods import macd



FILENAME = "BTC-DAILY.csv"


def run() -> None:
      dataset = read_csv(filename=FILENAME)

      macd(dataset)

      #print(dataset)





if __name__ == "__main__":
      run()