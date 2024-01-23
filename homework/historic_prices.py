import typing
import datetime
import random
import statistics
from functools import reduce
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

    @staticmethod
    def get_scenario(returns: typing.Sequence[float], start_value: float, k: int = 240) -> float:
        """
        Returns a scenario list of projected prices based on available returns.
        :param returns: A sequence of returns.
        :type returns: List of numbers.
        :param start_value: Starting value of the asset.
        :type start_value: float
        :param k: Length of projection in months.
        :type k: int
        :return: Projected value
        """
        returns = random.choices(returns, k=k)
        return reduce(lambda x, y: x * (1 + y), returns, start_value)

    def forecast(self, ticker: str, num_of_scenarios: int = 1000, months: int = 240,
                 *args, **kwargs) -> typing.Dict:
        """
        Returns projected prices using historical monthly changes.
        :param ticker: Ticker
        :param num_of_scenarios: Number of scenarios to run.
        :param months: Number of future months for the projection.
        :return: Best case price.
        """
        historical_prices = self.get_historic_daily_prices(ticker)["Close"]
        if historical_prices.empty:
            return {'error': f'No price data found for ticker {ticker}.'}
        latest_price = historical_prices[historical_prices.index.max()]
        month_end_prices = historical_prices.resample("M").last().sort_index()
        returns = month_end_prices.pct_change().dropna().to_list()
        scenarios = [
            self.get_scenario(returns, latest_price, months)
            for _ in range(num_of_scenarios)
        ]

        return {
            "max": max(scenarios),
            "min": min(scenarios),
            "median": statistics.median(scenarios),
        }
