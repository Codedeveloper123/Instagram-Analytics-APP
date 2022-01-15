from datetime import datetime, timedelta

## This file contains all the statistic functions I run on the data.
def engagment_per_post(totalengagmentnumber, totalnumberofPosts):
    rate = totalengagmentnumber / totalnumberofPosts
    return rate


def engagment_per_follower(totalengagmentnumber, totalnumberoffollowers):
    rate = totalengagmentnumber / totalnumberoffollowers
    return rate


def reach_rate(reachnumber, followers):
    rate = reachnumber / followers
    rate = rate * 100
    return rate


def calculate_time_difference(date1, date2):
    duration = date1 - date2
    time_difference_in_minutes = duration / timedelta(minutes=1)
    hours = time_difference_in_minutes / 60
    days = 0
    if hours > 24:
        days = int(hours / 24)
        return "{} days.".format(days)
    else:
        return "{} hours.".format(hours)


def follower_growth_rate(followercount1, followercount2, date1, date2):
    rate = followercount1 / followercount2
    rate = rate * 100
    timedifference = calculate_time_difference(date1, date2)
    return "Follower growth rate in last {} since script was run is {} % ".format(
        timedifference, rate
    )
