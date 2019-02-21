"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.


def countSwaps(a):

    swaps = 0

    for counter in a:
        for counter in range(len(a)-1):
            if a[counter] > a[counter+1]:
                a[counter], a[counter+1] = a[counter+1], a[counter]
                swaps += 1

    return print("Array is sorted in %i swaps.\nFirst Element: %i\nLast Element: %i" % (swaps, a[0], a[-1]))


if __name__ == '__main__':
    n = int(input("Input number of values in list: "))

    a = list(map(int, input("Input the values in list: ").rstrip().split()))

    countSwaps(a)
