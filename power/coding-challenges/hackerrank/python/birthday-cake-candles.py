def birthday_cake_candles(arr):
    return arr.count(max(arr))

arr = [4, 4, 5, 6, 1, 2, 6, 6, 0]
print("birthday_cake_candles():", birthday_cake_candles(arr))

"""
birthday_cake_candles(): 3
"""