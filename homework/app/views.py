import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from jsonschema.exceptions import ValidationError
from predictors import PricePredictions
from .validation import PricePredictionsParametersValidator


def historic_pricer_forecast(request) -> HttpResponse:
    """Returns response for GET request."""
    params = dict(request.GET.items())
    params = {k: int(v) if v.isdigit() else v for k, v in params.items()}
    try:
        PricePredictionsParametersValidator(params)
    except ValidationError as e:
        return HttpResponseBadRequest(f'Error while validating parameters: {e}')

    return JsonResponse(PricePredictions().predict_prices(**params))
