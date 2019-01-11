"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):

    # consider we have more rotations than the len(a)
    # this simplifies it to the minimum amount of rotations
    # 5 rotations for len(a) if 5 is 0 rotations
    left = d % len(a)
    # start at a[2] and end at a[2]
    return a[left:] + a[:left]

    # # Initial implementation though O(n^2) roughly
    # for counter in range(d):
    #     temp = a[0]
    #     for counter in range(len(a)-1):
    #         a[counter] = a[counter+1]
    #     a[len(a)-1] = temp

    # return a


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
