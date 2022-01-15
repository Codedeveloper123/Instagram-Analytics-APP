from defines import getCreds, makeApiCall
from get_user_media import WebScrapper
import datetime
import sqlite3

conn = sqlite3.connect("instagramstats.db")
c = conn.cursor()
# c.execute(
# """CREATE TABLE instagramstatistics(date DATE,posts REAL,followers REAL,engagement REAL,reach REAL)"""
# )
# c.execute(
# """CREATE TABLE latestpoststats(date DATE,engagment REAL,impressions REAL,reach REAL)"""
# )
# c.execute("""DROP TABLE latestpoststats""")
def getAllRelevantData(params):
    webscrapper = WebScrapper()
    buisness_discovery = webscrapper.getAccountInfo(params)
    username = buisness_discovery["json_data"]["business_discovery"]["username"]
    numberOfPosts = buisness_discovery["json_data"]["business_discovery"]["media_count"]
    numberoffollowers = buisness_discovery["json_data"]["business_discovery"][
        "followers_count"
    ]
    numberofpeopletheyfollow = buisness_discovery["json_data"]["business_discovery"][
        "follows_count"
    ]
    medialist = []
    engagmentnumber = 0
    reachnumber = 0
    respons = webscrapper.getAllUserMediaIds(params, medialist, pagingURL="")
    response = webscrapper.getUserMedia2(params)
    latestpostdate = response["json_data"]["data"][0]["timestamp"]
    params["latest_media_id"] = response["json_data"]["data"][0]["id"]
    params["metric"] = "engagement,impressions,reach"
    latestpostdata = webscrapper.getMediaInsights(params)
    latestpostengagment = latestpostdata["json_data"]["data"][0]["values"][0]["value"]
    latestpostreach = latestpostdata["json_data"]["data"][2]["values"][0]["value"]
    latestpostimpressions = latestpostdata["json_data"]["data"][1]["values"][0]["value"]

    while len(respons) < numberOfPosts:
        respons = webscrapper.getAllUserMediaIds(
            params, respons, response["json_data"]["paging"]["next"]
        )
        response = webscrapper.getUserMedia2(
            params, response["json_data"]["paging"]["next"]
        )
    for mediaid in respons:
        params["latest_media_id"] = mediaid
        params["metric"] = "engagement,impressions,reach,saved"
        stats = webscrapper.getMediaInsights(params)
        engagmentnumber = (
            stats["json_data"]["data"][0]["values"][0]["value"] + engagmentnumber
        )
        reachnumber = stats["json_data"]["data"][2]["values"][0]["value"] + reachnumber
    currentdate = datetime.datetime.now()
    c.execute(
        """INSERT INTO instagramstatistics VALUES(?,?,?,?,?)""",
        (currentdate, numberOfPosts, numberoffollowers, engagmentnumber, reachnumber),
    )
    c.execute(
        """INSERT INTO latestpoststats VALUES(?,?,?,?)""",
        (
            latestpostdate,
            latestpostengagment,
            latestpostimpressions,
            latestpostreach,
        ),
    )


parms = getCreds()
getAllRelevantData(parms)
conn.commit()