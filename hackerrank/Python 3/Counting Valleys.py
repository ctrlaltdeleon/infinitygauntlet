"""
Created 1/6/2019

@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):

    inValley = False
    vallies = 0
    height = 0

    for step in s:
        if step == 'U':
            height += 1
        else:
            height -= 1

        # checks everytime we go down, no important of checking up
        if not inValley:
            if height < 0:
                inValley = True
        elif height == 0:
            inValley = False
            vallies += 1

    return vallies


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
