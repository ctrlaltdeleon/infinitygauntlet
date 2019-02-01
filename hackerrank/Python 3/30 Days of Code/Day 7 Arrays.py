"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reversal(arr):

    arr.reverse()
    # for everything in the array, join the element with a " " and continue
    solution = ' '.join(str(_) for _ in arr)

    return solution

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reversal(arr))

    # efficient one liner for the problem
    # map a string to the list, starting from the back
    # print(" ".join(map(str, arr[::-1])))