"""
@author: acfromspace
"""


def miniMaxSum(arr):
    mini, maxi = 0, 0
    arr.sort()
    for index in arr[:-1]:
        mini += index
    maxi = mini - arr[0] + arr[-1]
    print(mini, maxi)


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
