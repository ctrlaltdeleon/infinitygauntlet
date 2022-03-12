"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    score = [0, 0]
    for index in range(len(a)):
        if a[index] > b[index]:
            score[0] += 1
        elif b[index] > a[index]:
            score[1] += 1
    return score


a = [5, 6, 7]
b = [3, 6, 10]
print("comparetriplets():", compareTriplets(a, b))
