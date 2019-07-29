"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def reversal(arr):
    arr.reverse()
    solution = ' '.join(str(_) for _ in arr)
    return solution


n = int(input())
arr = list(map(int, input().rstrip().split()))
print(reversal(arr))

"""
Pythonic solution:
    print(" ".join(map(str, arr[::-1])))
"""
