"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):

    # from the list, map everything into a strings then join them together into 1 string
    journey = ''.join(c)
    # journey = ''.join(map(str, c))
    return journey.count('00') + journey.count('1')


if __name__ == '__main__':

    # n = int(input("Input number of clouds: "))

    c = input("Input thunder (1) vs cumulus (0): ")
    # c = list(map(int, input().rstrip().split()))

    print("Number of jumps:", jumpingOnClouds(c))

# 7
# 0 0 1 0 0 1 0
