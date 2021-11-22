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


def shortest_interval(activities: list):
    N = len(activities)
    # activities_with_interval = [[activities[i][0], activities[i][1], abs(activities[i][0] - activities[i][1])] for
    # i in range(N)]
    i = 0
    sorted_activities = sorted(activities, key=lambda x: abs(x[0] - x[1]))

    selected = [sorted_activities[0]]
    for m in range(N):
        if sorted_activities[m][0] >= sorted_activities[i][1]:
            selected.append(sorted_activities[m])
            i = m
    return selected
