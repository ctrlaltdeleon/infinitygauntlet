"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def repeated_string(s, n):
    # Original string * num of times repeated till n (floored) + leftover.
    # n = 10, s = aba
    # (2 "a"s * 3 whole strings) + 1 leftover "a" = 7
    return s.count('a')*(n//len(s))+s[:n % len(s)].count('a')


s = input("""String containing 'a': """)
n = int(input("Max characters to be filled out by string: "))
print("repeated_string(): ", repeated_string(s, n))

"""
INPUT:
aba
10

OUTPUT:
7

EXPLANATION:
abaabaabaa

Amount of "a" in the string of width 10 is 7.
"""
