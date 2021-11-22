from greedy_selection import earliest_start_time, shortest_interval
from kruskal import run_kruskal
from dfs import run_detect_cycle,run_scc
# Driver code
# data = [[5, 9], [1, 9], [0, 1], [0, 12], [0, 11], [2, 7], [9, 15]]

# data = [[5, 9], [12, 15], [5, 6], [11, 12], [3, 11], [8, 14], [11, 13]]  # Rayhan
# data = [[2, 6], [2, 12], [1, 2], [9, 12], [8, 13], [3, 6], [2, 5]]  # Labid
if __name__ == '__main__':
    # run_dfs()
    run_kruskal()
    # run_detect_cycle()
    # run_scc()
    # print('Earliest Start time: ', end='')
    # print(earliest_start_time(data))
    # print('Shortest interval: ', end='')
    # print(shortest_interval(data))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
