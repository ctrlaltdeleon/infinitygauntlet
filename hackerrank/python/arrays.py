"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.


def reverseArray(a):

    # reversed = []

    # for counter in range(len(a)-1, -1, -1):
    #     reversed.append(a[counter])

    # return reversed

    return a.reverse()


if __name__ == '__main__':
    arr_count = int(input("Array count: "))

    arr = list(
        map(int, input("Array itself (spaces in between values): ").rstrip().split()))

    print("Array reversed: ", reverseArray(arr))
