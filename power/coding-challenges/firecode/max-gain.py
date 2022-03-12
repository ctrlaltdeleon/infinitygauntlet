"""
@author: acfromspace
"""


def max_gain(input_list):
    if len(input_list) == 1:
        return 0
    maxi = 0
    mini = input_list[0]
    for i in range(len(input_list)):
        mini = min(mini, input_list[i])
        maxi = max(maxi, input_list[i] - mini)
    return 0 if maxi < 0 else maxi


gains = [10, 50, 100, 20, 40, 200, 0, 5]
print("max_gain():", max_gain(gains))
