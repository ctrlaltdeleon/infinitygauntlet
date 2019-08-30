#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'areAlmostEquivalent' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY s
#  2. STRING_ARRAY t
#

import collections


def areAlmostEquivalent(s, t):
    yeet = Counter(s)
    print(yeet)
    return yeet


s = "aabaab"
t = "bbabbc"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s_count = int(input().strip())

#     s = []

#     for _ in range(s_count):
#         s_item = input()
#         s.append(s_item)

#     t_count = int(input().strip())

#     t = []

#     for _ in range(t_count):
#         t_item = input()
#         t.append(t_item)

#     result = areAlmostEquivalent(s, t)

#     fptr.write('\n'.join(result))
#     fptr.write('\n')

#     fptr.close()
