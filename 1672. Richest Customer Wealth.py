from ast import List


def maximumWealth(accounts):
    max_arr = []
    for i in accounts:
        max_arr += sum(i)
    return max(max_arr)

accounts = [[1,2,3],[3,2,1,3]]
maximumWealth(accounts)

