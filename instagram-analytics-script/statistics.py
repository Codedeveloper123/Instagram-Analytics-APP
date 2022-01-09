from datetime import datetime, timedelta


def engagmentPerPost(totalengagmentnumber, totalnumberofPosts):
    rate = totalengagmentnumber / totalnumberofPosts
    return rate


def engagmentperfollower(totalengagmentnumber, totalnumberoffollowers):
    rate = totalengagmentnumber / totalnumberoffollowers
    return rate


def reachrate(reachnumber, followers):
    rate = reachnumber / followers
    rate = rate * 100
    return rate


def calculateTimeDifference(date1, date2):
    duration = date1 - date2
    time_difference_in_minutes = duration / timedelta(minutes=1)
    hours = time_difference_in_minutes / 60
    days = 0
    if hours > 24:
        days = int(hours / 24)
        return "{} days.".format(days)
    else:
        return "{} hours.".format(hours)


def followergrowthrate(followercount1, followercount2, date1, date2):
    rate = followercount1 / followercount2
    rate = rate * 100
    timedifference = calculateTimeDifference(date1, date2)
    return "Follower growth rate in last {} since script was run is {} % ".format(
        timedifference, rate
    )
