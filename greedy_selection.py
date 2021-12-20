# This file contains code for greedy activity selection algorithm
# Assignment: 2
# Lab: 1

def earliest_start_time(activities: list):
    N = len(activities)
    sorted_activities = sorted(activities, key=lambda x: x[0])
    i = 0
    selected = [sorted_activities[0]]
    for m in range(1, N):
        if sorted_activities[m][0] >= sorted_activities[i][1]:
            selected.append(sorted_activities[m])
            i = m
    return selected


def earliest_end_time(activities: list):
    N = len(activities)
    sorted_activities = sorted(activities, key=lambda x: x[1])
    i = 0
    selected = [sorted_activities[0]]
    for m in range(1, N):
        if sorted_activities[m][0] >= sorted_activities[i][1]:
            selected.append(sorted_activities[m])
            i = m
    return selected


def shortest_interval(activities: list):
    N = len(activities)
    i = 0
    sorted_activities = sorted(activities, key=lambda x: abs(x[0] - x[1]))

    selected = [sorted_activities[0]]
    for m in range(N):
        if sorted_activities[m][0] >= sorted_activities[i][1]:
            selected.append(sorted_activities[m])
            i = m
    return selected


def FractionalKnapsack(wp, W):
    n = len(wp)
    profit = 0
    weight = W
    sorted_wp = sorted(wp, key=lambda x: x[1] / x[0])
    for i in range(1, n):
        if sorted_wp[i][0] <= weight:
            profit += sorted_wp[i][1]
            weight -= sorted_wp[i][0]
        else:
            profit += weight * (sorted_wp[i][0]/sorted_wp[i][1])
            weight = 0
            break
    return profit
