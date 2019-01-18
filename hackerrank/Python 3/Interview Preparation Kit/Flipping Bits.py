"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.


def flippingBits(n):

    # this number is (2**32)-1
    # unsigned integers given which is 32
    # 2**32 = 4294967296
    # to flip is to just minus 1
    THE_FLIPPING = 4294967295

    # ^ = bitwise XOR
    return n ^ THE_FLIPPING


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Number of queries to be inputtted: "))

    for q_itr in range(q):
        n = int(input("Insert random numbers to be flipped: "))

        result = flippingBits(n)
        print("Result:", result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
