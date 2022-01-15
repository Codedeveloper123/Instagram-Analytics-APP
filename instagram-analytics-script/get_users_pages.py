from defines import get_creds, make_api_call


def get_users_pages(params):
    """Get facebook pages for a user

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams["access_token"] = params["access_token"]
    url = params["endpoint_base"] + "me/accounts"
    return make_api_call(url, endpointParams, params["debug"])


params = get_creds()
params["debug"] = "yes"
response = get_users_pages(params)

print("\n---- FACEBOOK PAGE INFO ----\n")  # section heading
print("Page Name:")  # label
print(response["json_data"]["data"][0]["name"])  # display name
print("\nPage Category:")  # label
print(response["json_data"]["data"][0]["category"])  # display category
print("\nPage Id:")  # label
print(response["json_data"]["data"][0]["id"])  # display id
