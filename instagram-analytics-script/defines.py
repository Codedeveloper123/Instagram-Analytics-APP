import requests
import json
import dotenv
import os
from requests.models import Response


def get_creds():
    dotenv.load_dotenv(".env")

    creds = dict()
    creds["access_token"] = os.environ["Access_Token"]
    creds["client_id"] = os.environ["client_id"]
    creds["client_secret"] = os.environ["client_secret"]
    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["graph_version"] = "v12.0"
    creds["endpoint_base"] = creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "none"
    creds["page_id"] = os.environ["page_id"]
    creds["page_access_token"] = os.environ["page_access_token"]
    creds["instagram_account"] = os.environ["instagram_account"]
    creds["ig_username"] = os.environ["ig_username"]
    return creds


def make_api_call(url, endpointParams, debug="none"):
    data = requests.get(url, endpointParams)
    if data.status_code == 400:
        print(
            "Your authentication access has been expired generate a new access token if that dosen't solve issue generate new page access token"
        )
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dumps(endpointParams, indent=4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent=4)
    if "yes" == debug:
        display_api_call_data(response)
    return response


def display_api_call_data(response):
    print("\nURL: ")
    print(response["url"])
    print("\nEndpoint Params: ")
    print(response["endpoint_params_pretty"])
    print("\nResponse: ")
    print(response["json_data_pretty"])
