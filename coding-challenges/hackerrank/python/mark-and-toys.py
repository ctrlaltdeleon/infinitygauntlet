"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys


def maximum_toys(prices, k):
    prices.sort()
    cart = []
    for index in prices:
        if sum(cart)+index < k:
            cart.append(index)
    return len(cart)


if __name__ == '__main__':
    nk = input("Input number of items and budget: ").split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(
        map(int, input("Input the value of each item: ").rstrip().split()))
    print("maximum_toys():", maximum_toys(prices, k))
