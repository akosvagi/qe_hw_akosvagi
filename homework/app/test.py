import typing

from jsonschema.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from .validation import HistoricPricerForecastResponseValidator


class TestHistoricPricerForecastEndpoint(TestCase):
    """
    Unit tests for the endpoint.
    These can be run by the command `python manage.py test` from the root directory.
    """
    view_name = 'api/historic-pricer/forecast'

    valid_parameters = {'ticker': 'AAPL', 'num_of_scenarios': 1000, 'months': 240}
    invalid_ticker_params = {'ticker': 'abcdabcd', 'num_of_scenarios': 1000, 'months': 240}
    negative_num_of_scenarios = {'ticker': 'AAPL', 'num_of_scenarios': -10, 'months': 240}
    num_of_scenarios_over_limit = {'ticker': 'AAPL', 'num_of_scenarios': 100000, 'months': 240}

    def test_valid_request(self):
        response = self._get_response(self.valid_parameters)
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        try:
            HistoricPricerForecastResponseValidator(response_json)
            response_valid = True
        except ValidationError:
            response_valid = False
        self.assertTrue(response_valid)

        self.assertGreaterEqual(response_json['max'], response_json['median'])
        self.assertGreaterEqual(response_json['median'], response_json['min'])

    def test_negative_num_of_scenarios(self):
        """Should return status 400."""
        response = self._get_response(self.negative_num_of_scenarios)
        self.assertEqual(response.status_code, 400)

    def test_num_of_scenarios_over_limit(self):
        """Should return status 400."""
        response = self._get_response(self.num_of_scenarios_over_limit)
        self.assertEqual(response.status_code, 400)

    def test_invalid_ticker(self):
        response = self._get_response(self.invalid_ticker_params)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response)

    def _get_response(self, params: typing.Dict):
        suffix = '&'.join(f'{k}={v}' for k, v in params.items())
        response = self.client.get(reverse(self.view_name) + f'?{suffix}')
        return response
