import typing
import random
import pandas as pd
from historic_prices import HistoricPricer


class PricePredictions:

    def predict_prices(self, ticker, num_of_scenarios: int = 1000, months: int = 240,
                       prices: typing.Optional[pd.Series] = None) -> typing.Dict:
        """
        Returns predicted price statistics.
        :param ticker: Single ticker.
        :type ticker: str.
        :param num_of_scenarios: Number of scenarios to be generated.
        :type num_of_scenarios: int
        :param months: Length of prediction in months.
        :type months: int
        :param prices: Optional price data to override the historic pricer.
        :return: Price statistics.
        :rtype: dict.
        """
        prices = prices or HistoricPricer().get_historic_daily_prices(ticker)["Close"]

        if not isinstance(prices, pd.Series):
            raise TypeError(f'Price data must be pd.Series; got {type(prices)} instead.')
        elif prices.empty:
            return {'error': f'No price data found for ticker {ticker}.'}

        return self.forecast(prices, num_of_scenarios, months)

    def forecast(self, prices, num_of_scenarios: int = 1000, months: int = 240,
                 sample_by: str = 'M') -> typing.Dict:
        """
        Generates scenarios and returns price statistics (min, max, median).
        :param prices: Price data.
        :type prices: pd.Series indexed by dates.
        :param num_of_scenarios: Number of scenarios to run.
        :type num_of_scenarios: int.
        :param months: Number of future months for the projection.
        :type months: int.
        :param sample_by: Defines sampling resolution (monthly by default).
        :type sample_by: str
        :return: Best case price.
        """
        latest_price = prices[prices.index.max()]
        period_end_prices = prices.resample(sample_by).last().sort_index()
        returns = period_end_prices.pct_change().dropna().to_list()
        scenarios = [
            self._get_scenario(returns, latest_price, months)
            for _ in range(num_of_scenarios)
        ]
        final_prices = pd.Series([scenario[-1] for scenario in scenarios])

        return {
            "max": final_prices.max(),
            "min": final_prices.min(),
            "median": final_prices.median(),
        }

    @staticmethod
    def _get_scenario(returns: typing.Sequence[float], start_value: float, length: int = 240) -> typing.List[float]:
        """
        Returns a scenario (list of projected prices) based on available returns.
        :param returns: A sequence of returns.
        :type returns: List of numbers.
        :param start_value: Starting value of the asset.
        :type start_value: float
        :param length: Length of projection.
        :type length: int.
        :return: Projected price values.
        :rtype: list.
        """
        return_sample = random.choices(returns, k=length)
        return ((pd.Series(return_sample) + 1).cumprod() * start_value).to_list()
