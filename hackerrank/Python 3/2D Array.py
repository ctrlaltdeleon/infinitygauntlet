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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
