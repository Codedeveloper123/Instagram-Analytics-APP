import requests
import json

from requests.models import Response


def getCreds():
    creds = dict()
    creds["access_token"] = "ACESS-Token #"
    creds["client_id"] = "FaceBook AP ID"
    creds["client_secret"] = "Facebook Ap Secret ID"
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
