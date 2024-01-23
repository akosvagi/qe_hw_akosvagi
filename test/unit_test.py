import unittest
import random
import pandas as pd
from homework.historic_prices import HistoricPricer


class HistoricPricerForecast(unittest.TestCase):

    valid_ticker = 'AAPL'
    invalid_ticker = 'sfsdfzs'

    def setUp(self):
        random.seed(10)
        self.pricer = HistoricPricer()

    def test_get_month_end_prices(self):
        result = self.pricer.forecast(self.valid_ticker)
        self.assertGreaterEqual(result['max'], result['median'])
        self.assertGreaterEqual(result['median'], result['min'])

    def test_invalid_ticker(self):
        result = self.pricer.forecast(self.invalid_ticker)
        self.assertTrue('error' in result)

    def test_get_historic_daily_prices(self):
        result = self.pricer.get_historic_daily_prices(self.valid_ticker)
        self.assertTrue(isinstance(result, pd.DataFrame))
