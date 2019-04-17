"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys


def luck_balance(k, contests):
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


nk = input(
    "Input number of contests and number of important contests to at least lose: ").split()
n = int(nk[0])
k = int(nk[1])
contests = []
for index in range(n):
    contests.append(list(map(int, input(
        "Input points and importance (0 is not important, 1 is) for contest %i: " % (index+1)).rstrip().split())))
print("luck_balance():", luck_balance(k, contests))
