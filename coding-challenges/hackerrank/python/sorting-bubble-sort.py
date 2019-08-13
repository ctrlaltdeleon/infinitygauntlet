"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def count_swaps(a):
    swaps = 0
    for index in a:
        for index in range(len(a)-1):
            if a[index] > a[index+1]:
                a[index], a[index+1] = a[index+1], a[index]
                swaps += 1
    return print("Array is sorted in %i swaps.\nFirst Element: %i\nLast Element: %i" % (swaps, a[0], a[-1]))


n = int(input("Input number of values in list: "))
a = list(map(int, input("Input the values in list: ").rstrip().split()))
count_swaps(a)
