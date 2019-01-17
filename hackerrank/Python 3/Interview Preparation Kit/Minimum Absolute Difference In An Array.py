"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):

    # # complexity is horrible :(
    # stock = []
    # min = math.inf

    # for i in arr:
    #     for j in arr:
    #         stock.append(abs(i-j))

    # for i in stock:
    #     if i < min and i is not 0:
    #         min = i

    # return min

    arr.sort()

    return min([abs(arr[counter+1] - arr[counter]) for counter in range(len(arr)-1)])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Input number of values: "))

    arr = list(
        map(int, input("Array of values to be multiplied: ").rstrip().split()))

    print("Minimum absolute difference:", minimumAbsoluteDifference(arr))

    # result = minimumAbsoluteDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
