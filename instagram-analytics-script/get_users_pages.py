from defines import getCreds, makeApiCall


def getUsersPages(params):
    """Get facebook pages for a user

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams["access_token"] = params["access_token"]
    url = params["endpoint_base"] + "me/accounts"
    return makeApiCall(url, endpointParams, params["debug"])


params = getCreds()
params["debug"] = "yes"
response = getUsersPages(params)

print("\n---- FACEBOOK PAGE INFO ----\n")  # section heading
print("Page Name:")  # label
print(response["json_data"]["data"][0]["name"])  # display name
print("\nPage Category:")  # label
print(response["json_data"]["data"][0]["category"])  # display category
print("\nPage Id:")  # label
print(response["json_data"]["data"][0]["id"])  # display id