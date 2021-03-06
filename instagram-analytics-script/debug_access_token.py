from defines import get_creds, make_api_call
import datetime

# This function is usefuel to get information on the access token you are currently using.
def debug_access_token(params):
    """Get info on an access token
    API Endpoint:
        https://graph.facebook.com/
        debug_token?input_token ={input-token}&access_token={valid-access-token}
    Returns:
        object: data from the endpoint

    """
    endpointParams = dict()
    endpointParams["input_token"] = params["access_token"]
    endpointParams["access_token"] = params["access_token"]
    url = params["graph_domain"] + "/debug_token"
    return make_api_call(url, endpointParams, params["debug"])


params = get_creds()
params["debug"] = "yes"
response = debug_access_token(params)
print("\n Data Access Expires at: ")
print(
    datetime.datetime.fromtimestamp(
        response["json_data"]["data"]["data_access_expires_at"]
    )
)
print("\n Token Access Expires at: ")
print(datetime.datetime.fromtimestamp(response["json_data"]["data"]["expires_at"]))
