import yfinance as yf
import pandas as pd

def main() -> None:
    intc = yf.Ticker("BTC-USD")
    intc_history: pd.DataFrame = intc.history(period="5y")
    # print(type(intc_history))
    intc_history.to_csv("btc_usd_data.csv")

    return

if __name__ == "__main__":
    main()
