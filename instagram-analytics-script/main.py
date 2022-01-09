from statistics import (
    engagmentPerPost,
    engagmentperfollower,
    reachrate,
    calculateTimeDifference,
    followergrowthrate,
)
from defines import getCreds
from webscraper import getAllRelevantData
import sqlite3
from datetime import datetime
from dateutil.parser import parse
import functools

conn = sqlite3.connect("instagramstats.db")
c = conn.cursor()
c.execute("""SELECT posts FROM instagramstatistics""")
total_number_of_posts = c.fetchall()
c.execute("""SELECT followers FROM instagramstatistics""")
total_number_of_followers = c.fetchall()
c.execute("""SELECT engagement FROM instagramstatistics""")
total_number_of_engagment = c.fetchall()
c.execute("""SELECT reach FROM latestpoststats""")
total_number_of_reach = c.fetchall()
c.execute("""SELECT date FROM latestpoststats""")
post_dates = c.fetchall()
c.execute("""SELECT date FROM instagramstatistics""")
dates_script_ran = c.fetchall()
current_date = dates_script_ran[-1]
last_current_date = dates_script_ran[-2]
lastdate = last_current_date[0]
todays_date = current_date[0]
post_date = post_dates[-1]
latestpostdate = post_date[0]
posts_number = total_number_of_posts[-1]
enagment_number = total_number_of_engagment[-1]
follower_number = total_number_of_followers[-1]
last_follower_number = total_number_of_followers[-2]
lastfollower = last_follower_number[0]
reach_number = total_number_of_reach[-1]
engage = enagment_number[0]
posts = posts_number[0]
follower = follower_number[0]
reach = reach_number[0]
datetime_todays_date = parse(todays_date)
datetime_last_date = parse(lastdate)
average_engagment_per_post = engagmentPerPost(engage, posts)
average_engagment_per_follower = engagmentperfollower(engage, follower)
number_of_followers_that_see_post = reachrate(reach, follower)
followers_gained_since_last_post = followergrowthrate(
    follower, lastfollower, datetime_todays_date, datetime_last_date
)
firststat = "The reach rate for the latest post  is {}%. ".format(
    number_of_followers_that_see_post
)
secondstat = "The average engagment per post is {}. ".format(average_engagment_per_post)
thirdstat = "The average engagment per follower is {}. ".format(
    average_engagment_per_follower
)
print("\n---- Statistics -----\n")
print(firststat)
print(secondstat)
print(thirdstat)
print(
    followers_gained_since_last_post
    + "if it is 100%"
    + " then the follower count has not changed"
)
conn.close()
