from data import read_csv
from methods import macd, signal, analyze_macd, display_chart, simulate_investment, simulate_investment_rsi



FILENAME = "xauusd_d.csv"
LABEL = "BTC"



def main() -> None:

      
      dataset = read_csv(filename=FILENAME)

      dataset_display = dataset.tail(1000)

      macd_values = macd(dataset["close"])
      signal_values = signal(macd_values)


      buy_points, sell_points, intersection_points = analyze_macd(macd_values, signal_values, dataset_display)

      final_balance = simulate_investment(intersection_points, dataset_display)
      print("Final balance after simulation:", final_balance)
      print("\n \n")

      final_balance = simulate_investment_rsi(intersection_points, dataset_display)
      print("Final balance after simulation:", final_balance)


      
      # wykres 1000 dni
      display_chart(macd_values, signal_values, dataset_display, buy_points, sell_points, intersection_points, LABEL)
      
      # wykres 500 dni

      buy_points, sell_points, intersection_points = analyze_macd(macd_values, signal_values, dataset_display, 2)

      display_chart(macd_values, signal_values, dataset_display, buy_points, sell_points, intersection_points, LABEL, 500)


      # wykres 100 dni

      buy_points, sell_points, intersection_points = analyze_macd(macd_values, signal_values, dataset_display, 10)

      display_chart(macd_values, signal_values, dataset_display, buy_points, sell_points, intersection_points, LABEL, 100)

   



if __name__ == "__main__":
      main()

