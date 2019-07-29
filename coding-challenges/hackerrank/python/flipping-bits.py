"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys


def flipping_bits(n):
    # This number is (2**32)-1.
    # Unsigned integers given which is 32.
    # 2**32 = 4294967296.
    # To flip is to just minus 1.
    # 4294967296 - 1 = 4294967295
    THE_FLIPPING = 4294967295
    # ^ = bitwise XOR
    return n ^ THE_FLIPPING


q = int(input("Number of queries to be inputted: "))
for q_itr in range(q):
    n = int(input("Insert random numbers to be flipped: "))
    result = flipping_bits(n)
    print("flipping_bits():", result)
