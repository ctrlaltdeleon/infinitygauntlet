def mini_max_sum(arr):
    mini, maxi = 0, 0
    arr.sort()
    for index in arr[:-1]:
        mini += index
    maxi = mini - arr[0] + arr[-1]
    print(mini, maxi)

arr = [1, 2, 3, 4, 5]
mini_max_sum(arr)

"""
10 14
"""