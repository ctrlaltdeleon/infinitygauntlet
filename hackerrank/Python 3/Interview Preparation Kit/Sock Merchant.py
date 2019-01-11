"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):

    # provides remove() and add()
    stock = set()
    pairs = 0

    for socks in ar:
        if socks in stock:
            stock.remove(socks)
            pairs += 1
        else:
            stock.add(socks)

    return pairs


if __name__ == '__main__':

    n = int(input("Number of socks: "))

    ar = list(
        map(int, input("Different socks (spaces in between): ").rstrip().split()))

    result = sockMerchant(n, ar)
