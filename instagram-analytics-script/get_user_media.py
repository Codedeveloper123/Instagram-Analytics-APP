from defines import makeApiCall


class WebScrapper:
    def getAllUserMediaIds(self, params, mediaidlist, pagingURL=""):
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

    def getUserMedia2(self, params, pagingURL=""):
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

    def getAccountInfo(self, params):
        """Get info on a users account

        API Endpoint:
                https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
        Returns:
                object: data from the endpoint
        """
        endpointParams = dict()
        endpointParams["fields"] = (
            "business_discovery.username("
            + params["ig_username"]
            + "){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}"
        )
        endpointParams["access_token"] = params["access_token"]
        url = params["endpoint_base"] + params["instagram_account"]
        return makeApiCall(url, endpointParams, params["debug"])

    def getMediaInsights(self, params):
        """Get insights for a specific media id

        API Endpoint:
                https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}
        Returns:
                object: data from the endpoint
        """
        endpointParams = dict()  # parameter to send to the endpoint
        endpointParams["metric"] = params["metric"]  # fields to get back
        endpointParams["access_token"] = params["access_token"]  # access token
        url = params["endpoint_base"] + params["latest_media_id"] + "/insights"
        return makeApiCall(url, endpointParams, params["debug"])  # make the api call

    def getUserInsights(self, params):
        """Get insights for a users account

        API Endpoint:
                https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}
        Returns:
                object: data from the endpoint
        """
        endpointParams = dict()
        endpointParams["metric"] = "follower_count,impressions,profile_views,reach"
        endpointParams["period"] = "day"
        endpointParams["access_token"] = params["access_token"]
        url = params["endpoint_base"] + params["instagram_account"] + "/insights"
        return makeApiCall(url, endpointParams, params["debug"])
