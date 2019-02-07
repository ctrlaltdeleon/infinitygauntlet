"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):

    prices.sort()
    cart = []

    for counter in prices:
        if sum(cart)+counter < k:
            cart.append(counter)

    return len(cart)

    # # problem here was that it wasn't keeping track of the number of items correctly, only price
    # # the "counter" in the for loop iterates over the actual value not the index itself
    # prices.sort()
    # cart = 0

    # for counter in prices:
    #     cart += prices[counter]
    #     if cart >= k:
    #         break

    # return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input("Input number of items and budget: ").split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(
        map(int, input("Input the value of each item: ").rstrip().split()))

    print(maximumToys(prices, k))

    # result = maximumToys(prices, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
