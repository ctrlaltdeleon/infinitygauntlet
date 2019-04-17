"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys


def minimum_absolute_difference(arr):
    arr.sort()
    return min([abs(arr[index+1] - arr[index]) for index in range(len(arr)-1)])


n = int(input("Input number of values: "))
arr = list(
    map(int, input("Values to be finding the minimum absolute difference: ").rstrip().split()))
print("minimum_absolute_difference():", minimum_absolute_difference(arr))
