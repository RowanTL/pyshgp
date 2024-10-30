import yfinance as yf
import pandas as pd

def main() -> None:
    intc = yf.Ticker("intc")
    intc_history: pd.DataFrame = intc.history(period="1y")
    # print(type(intc_history))
    intc_history.to_csv("intc_data.csv")

    return

if __name__ == "__main__":
    main()
