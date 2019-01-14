"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):

    sum = []

    # 4x4 = 16 solutions
    for row in range(len(arr)-2):
        for col in range(len(arr)-2):
            # This is the hourglass shape
            sum.append(arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1]
                       [col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2])

    return max(sum)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        # input should be a 6 by 6 2D array
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
