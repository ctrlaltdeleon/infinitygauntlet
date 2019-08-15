"""
@author: acfromspace
"""


def birthdayCakeCandles(arr):
    return arr.count(max(arr))


arr = [4, 4, 5, 6, 1, 2, 6, 6, 0]
print("birthdayCakeCandles():", birthdayCakeCandles(arr))
