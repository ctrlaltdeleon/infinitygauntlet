"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    left_diag, right_diag = 0, 0
    for index in range(len(arr)):
        left_diag += arr[index][index]
        right_diag += arr[index][len(arr)-1-index]
    return abs(left_diag - right_diag)


arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
print("diagonalDifference():", diagonalDifference(arr))
