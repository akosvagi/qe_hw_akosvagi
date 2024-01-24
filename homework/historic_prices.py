import pandas as pd
import yfinance as yf


class HistoricPricer:

    @staticmethod
    def get_historic_daily_prices(ticker: str, period="max") -> pd.DataFrame:
        """
        Return a DataFrame with the available historic prices of a specific ticker.
        :param ticker: Ticker.
        :type ticker: str.
        :param period: Period for fetching price data.
        :type period: str.
        """
        ticker = yf.Ticker(ticker)
        return ticker.history(period=period)
