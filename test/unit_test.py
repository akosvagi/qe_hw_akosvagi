import unittest
import random
from homework.predictors import PricePredictions


class TestPricePredictions(unittest.TestCase):

    valid_ticker = 'AAPL'
    invalid_ticker = 'abcd1234!$%'

    def setUp(self):
        random.seed(10)
        self.predictor = PricePredictions()

    def test_get_month_end_prices(self):
        """Valid tickers should return the statistics in a dict."""
        result = self.predictor.predict_prices(self.valid_ticker)
        self.assertIsInstance(result, dict)
        self.assertGreaterEqual(result['max'], result['median'])
        self.assertGreaterEqual(result['median'], result['min'])

    def test_invalid_ticker(self):
        """Invalid tickers should return a dict with an error."""
        result = self.predictor.predict_prices(self.invalid_ticker)
        self.assertIsInstance(result, dict)
        self.assertTrue('error' in result)

    def test_statistics_are_same_for_one_scenario(self):
        """For a single scenario, all statistics should be the same."""
        result = self.predictor.predict_prices(self.valid_ticker, num_of_scenarios=1)
        self.assertEqual(result['max'], result['median'])
        self.assertEqual(result['median'], result['min'])
