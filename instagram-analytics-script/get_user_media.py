from defines import getCreds, makeApiCall


def getAllUserMediaIds(params, mediaidlist, pagingURL=""):
    """Get users media

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams[
        "fields"
    ] = "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username"  # fields to get back
    endpointParams["access_token"] = params["access_token"]
    if "" == pagingURL:  # get first page
        url = (
            params["endpoint_base"] + params["instagram_account"] + "/media"
        )  # endpoint url
    else:  # get specific page
        url = pagingURL
    response = makeApiCall(url, endpointParams, params["debug"])
    for post in response["json_data"]["data"]:
        mediaidlist.append(post["id"])
    return mediaidlist


def getUserMedia2(params, pagingURL=""):
    """Get users media

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams[
        "fields"
    ] = "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username"  # fields to get back
    endpointParams["access_token"] = params["access_token"]
    if "" == pagingURL:  # get first page
        url = (
            params["endpoint_base"] + params["instagram_account"] + "/media"
        )  # endpoint url
    else:  # get specific page
        url = pagingURL
    return makeApiCall(url, endpointParams, params["debug"])
