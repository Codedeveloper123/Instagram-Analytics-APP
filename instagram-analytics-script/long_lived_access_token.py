from defines import get_creds, make_api_call


def get_long_lived_access_token(params):
    """Get long lived access token

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams["grant_type"] = "fb_exchange_token"
    endpointParams["client_id"] = params["client_id"]
    endpointParams["client_secret"] = params["client_secret"]
    endpointParams["fb_exchange_token"] = params["access_token"]
    url = params["endpoint_base"] + "oauth/access_token"
    return make_api_call(url, endpointParams, params["debug"])


params = get_creds()
response = get_long_lived_access_token(params)
print("\n ---- ACCESS TOKEN INFO ----\n")  # section header
print("Access Token:")  # label
print(response["json_data"]["access_token"])  # display access token
