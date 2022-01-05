import requests
import json

from requests.models import Response


def getCreds():
    creds = dict()
    creds[
        "access_token"
    ] = "EAALq4Ha3VOQBANKPBLDXoC09TEZBsqwkUZCjbbYT1n3B69Vbv6YTKDzM9RZBdqqIdC88CKBBLYMPCs06V5OJAtdlgzYZC8gBZBQQpjxeeVWpRHjKE1MBqa6ovxVaIELyS2hsQIeeMnXnuJzYz6jD3EAOQN1QZC3ayq9cRUZCR83Rw1uySmQ2o8JqS6e2q8nWhhgWRbXVUcxVxuwJ1PzdJyb"
    creds["client_id"] = "821199738721508"
    creds["client_secret"] = "a109b5ed1861bb3fc544ab1e6d0409d2"
    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["graph_version"] = "v12.0"
    creds["endpoint_base"] = creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "none"
    creds["page_id"] = "104070632162114"
    creds[
        "page_access_token"
    ] = "EAALq4Ha3VOQBAN8u9G5TUFbQvAqbjVZB7Awf6EHtNR9HxpBpCbLm0pwHx0tZCq3RnEayQvesm4CyR66lz160iIRQi5rU2c58ochqiUVYIhwporwFzuETaZARIxg2zYZC3zTctFaMxSWVflvviuLEmXFrfVf7Tki4lxdI4oGF0pWi6wrHyNoZAZB7qNeHQecZAaUMN6xWZA7ZBXWhDojvwqdKq"
    creds["instagram_account"] = "937109979701395"
    return creds


def makeApiCall(url, endpointParams, debug="none"):
    data = requests.get(url, endpointParams)
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dumps(endpointParams, indent=4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent=4)
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
