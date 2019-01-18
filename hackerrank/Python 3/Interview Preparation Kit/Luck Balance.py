"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.


def luckBalance(k, contests):

    # sort from greatest luck to least luck
    contests.sort(reverse=True)
    luck, important = 0, 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif important < k:
            luck += contest[0]
            important += 1
        else:
            luck -= contest[0]

    return luck


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input(
        "Input number of contests and number of important contests to at least lose: ").split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input(
            "Input points and importance for contest %i: " % (_+1)).rstrip().split())))

    print("Max amount of points attainable:", luckBalance(k, contests))

    # result = luckBalance(k, contests)

    # fptr.write(str(result) + '\n')

    # fptr.close()
