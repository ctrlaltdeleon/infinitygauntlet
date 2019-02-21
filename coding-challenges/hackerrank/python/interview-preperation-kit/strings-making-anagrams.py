"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.


def makeAnagram(a, b):

    # Obtain a data structure of a
    a = Counter(a)
    # Anything in "b" that "a" has, "subtract" from both
    # >>> c = Counter(a=4, b=2, c=0, d=-2)
    # >>> d = Counter(a=1, b=2, c=3, d=4)
    # >>> c.subtract(d)
    # >>> c
    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
    a.subtract(Counter(b))

    # Map absolute value on all values to note deletions
    # Take the sum of all the values as that's the deletions
    return sum(map(abs, a.values()))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input("Input string 1: ")

    b = input("Input string 2: ")

    print("Number of deletions made to create anagram:", makeAnagram(a, b))

    # fptr.write(str(res) + '\n')

    # fptr.close()
