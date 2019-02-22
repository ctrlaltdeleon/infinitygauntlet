"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys


def hourglass_sum(list_data):
    sum = []
    # 4x4 = 16 solutions.
    for row in range(len(list_data)-2):
        for col in range(len(list_data)-2):
            # This is the hourglass shape.
            sum.append(list_data[row][col] + list_data[row][col+1] + list_data[row][col+2] + list_data[row+1]
                       [col+1] + list_data[row+2][col] + list_data[row+2][col+1] + list_data[row+2][col+2])
    return max(sum)


list_data = []
for _ in range(6):
    # Input should be a 6 by 6 2D array.
    list_data.append(list(map(int, input(
        """Input row %i (6 integers, for example: "1 2 3 4 5 6"): """ % (_+1)).rstrip().split())))
print("hourglass_sum():", hourglass_sum(list_data))
