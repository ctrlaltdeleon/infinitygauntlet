#!/bin/python3

import math
import os
import random
import re
import sys


def isPossible(a, b, c, d):
    pairs = []
    pairs.append([a, b])
    while len(pairs) > 0:
        print(pairs)
        if pairs[0] == [c, d]:
            return "Yes"
        sumOfPairs = pairs[0][0] + pairs[0][1]
        if sumOfPairs <= c:
            pairs.append([sumOfPairs, pairs[0][1]])
        if sumOfPairs <= d:
            pairs.append([pairs[0][1], sumOfPairs])
        pairs.pop(0)
    print(pairs)
    return "No"


x1, y1 = 1, 4
x2, y2 = 5, 9
print(isPossible(x1, y1, x2, y2))
x1, y1 = 1, 1
x2, y2 = 6, 10
print(isPossible(x1, y1, x2, y2))
x1, y1 = 1, 1
x2, y2 = 3, 4
print(isPossible(x1, y1, x2, y2))

# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a = int(input().strip())
#     b = int(input().strip())
#     c = int(input().strip())
#     d = int(input().strip())
#     result = isPossible(a, b, c, d)
#     fptr.write(result + '\n')
#     fptr.close()
