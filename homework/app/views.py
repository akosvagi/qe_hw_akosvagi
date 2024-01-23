import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from jsonschema.exceptions import ValidationError
from historic_prices import HistoricPricer
from .validation import HistoricPricerForecastParametersValidator


def historic_pricer_forecast(request) -> HttpResponse:
    """Returns response for GET request."""
    params = dict(request.GET.items())
    params = {k: int(v) if v.isdigit() else v for k, v in params.items()}
    try:
        HistoricPricerForecastParametersValidator(params)
    except ValidationError as e:
        return HttpResponseBadRequest(f'Error while validating parameters: {e}')

    return JsonResponse(HistoricPricer().forecast(**params))
