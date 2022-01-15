from defines import make_api_call

## This class holds all functions related to getting data from API
class WebScrapper:
    def get_all_user_media_ids(self, params, mediaidlist, pagingURL=""):
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
        response = make_api_call(url, endpointParams, params["debug"])
        for post in response["json_data"]["data"]:
            mediaidlist.append(post["id"])
        return mediaidlist

    def get_specific_user_media_post(self, params, pagingURL=""):
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
        return make_api_call(url, endpointParams, params["debug"])

    def get_account_info(self, params):
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
        return make_api_call(url, endpointParams, params["debug"])

    def get_media_insights(self, params):
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
        return make_api_call(url, endpointParams, params["debug"])  # make the api call

    def get_user_insights(self, params):
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
        return make_api_call(url, endpointParams, params["debug"])
