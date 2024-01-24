import typing
from jsonschema import validate


class Validator:
    """Base class for validating a JSON schema"""

    schema: typing.Dict = {}

    def __init__(self, instance):

        validate(instance, self.schema)


class PricePredictionsParametersValidator(Validator):
    """Parameter schema for GET request."""

    schema = {
        'type': 'object',
        'required': ['ticker'],
        'properties': {
            'ticker': {
                'type': 'string',
            },
            'num_of_scenarios': {
                'type': 'integer',
                'minimum': 1,
                'maximum': 10000
            },
            'months': {
                'type': 'integer',
                'minimum': 1,
                'maximum': 1200
            }
        }
    }


class PricePredicitionsResponseValidator(Validator):
    """Parameter schema for response to GET request."""

    schema = {
        'type': 'object',
        'required': ['min', 'median', 'max'],
        'properties': {
            'min': {'type': 'number'},
            'median': {'type': 'number'},
            'max': {'type': 'number'}
        }
    }
