import pandas as pd
import yfinance as yf


class HistoricPricer():

    def get_historic_daily_prices(self, ticker: str) -> pd.DataFrame:
        """
        Return a DataFrame with the available historic prices of a specific ticker.
        """
        ticker = yf.Ticker(ticker)
        return ticker.history(period='max')
