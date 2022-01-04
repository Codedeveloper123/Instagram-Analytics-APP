import requests
import json

from requests.models import Response


def getCreds():
    creds = dict()
    creds[
        "access_token"
    ] = "EAALq4Ha3VOQBAOOcLZAmisCubEebyokkyuKBbuhngqZB54iTFd4YWYcKtxEOdJrc7bM0DhJjTqbkMmKYx4mi9QxquGrfFQPlFJHqG5cLlqpwbRuAJfIscHeoZAMZAZAzbykAg69o1qaIrAJvSpKGZCZA9ZAwxitoBvqprZAwIR6BRba6n2AJMRuZBTvacfNqpULXOCnEOzZBXSRdTF9GNoGacJe"
    creds["client_id"] = "821199738721508"
    creds["client_secret"] = "a109b5ed1861bb3fc544ab1e6d0409d2"
    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["graph_version"] = "v12.0"
    creds["endpoint_base"] = creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "none"
    return creds


def makeApiCall(url, endpointParams, debug="none"):
    data = requests.get(url, endpointParams)
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dump(endpointParams, indent=4)
    response["json_data"] = json.loads(data.content)
    response["kson_data_pretty"] = json.dump(response["json_data"], indent=4)
    if "yes" == debug:
        displayApiCallData(response)
    return response


def displayApiCallData(response):
    print("\nURL: ")
    print(response["url"])
    print("\nEndpoint Params: ")
    print(response["endpoint_params_pretty"])
    print("\nResponse: ")
    print(response["json_data_pretty"])
