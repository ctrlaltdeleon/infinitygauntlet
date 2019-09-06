#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


def areAlmostEquivalent(s, t):
    if len(s) == len(t):
        if all(c.islower() for c in s):
            if all(c.islower() for c in t):
                firstString = Counter(s)
                secondString = Counter(t)
                firstString.subtract(secondString)
                # `subtract` does what you think, the opposite is `update`.
                for index in firstString:
                    if firstString[index] > 3 or firstString[index] < -3:
                        return "No"
                return "Yes"
    return "No"

# Rules:
# 1. Equal length.
# 2. Only English lowercase letters.
# 3. Occurrences of a specific character must not differ > 3 or < -3.
# 4. If all is satisfied, return "YES", else "NO".


s = "aab4ab"
t = "bbabbc"
print(areAlmostEquivalent(s, t))
s = "aabbasfuf"
t = "bbabbc"
print(areAlmostEquivalent(s, t))
s = "yeet"
t = "joji"
print(areAlmostEquivalent(s, t))

# Complete the 'areAlmostEquivalent' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY s
#  2. STRING_ARRAY t

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
