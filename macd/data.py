import pandas as pd


BUY = 1
SELL = 0
INITIAL_BALANCE = 10000

def read_csv(filename : str) -> pd.DataFrame:
      return pd.read_csv(filename, usecols=["date", "close", "symbol"], nrows=1026).iloc[::-1].reset_index(drop=True)

def simulate_investment_better(intersection_points, dataset_display):
    balance = INITIAL_BALANCE
    holding = 0  # 0 for not holding, 1 for holding
    for point, value, action in intersection_points:
        if action == BUY and balance > dataset_display["close"].loc[point]:
            # Buy if the balance is enough and MACD indicates a buy signal
            holding = 1
            balance -= dataset_display["close"].loc[point]
            print(f"Bought at {point}, price: {dataset_display['close'].loc[point]}, balance: {balance}")
        elif action == SELL and holding == 1:
            # Sell if holding and MACD indicates a sell signal
            holding = 0
            balance += dataset_display["close"].loc[point]
            print(f"Sold at {point}, price: {dataset_display['close'].loc[point]}, balance: {balance}")
    return balance
      