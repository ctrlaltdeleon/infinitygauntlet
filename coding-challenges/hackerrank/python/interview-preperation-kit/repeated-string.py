"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):

    # original string * num of times repeated till n (floored) + leftover
    # n = 10, s = aba (3)
    # 2 * 3 + 1 = 7
    return s.count('a')*(n//len(s))+s[:n % len(s)].count('a')


if __name__ == '__main__':

    s = input("""String containing 'a': """)

    n = int(input("Max characters to be filled out by string: "))

    print("Number of letter 'a': ", repeatedString(s, n))
