"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def alternating_characters(s):
    deletions = 0
    for index, character in enumerate(s[:-1]):
        if s[index+1] == character:
            deletions += 1
    return deletions


q = int(input("Input number of strings: "))
for q_itr in range(q):
    s = input("Input string %i: " % (q_itr+1))
    print("alternating_characters():", alternating_characters(s))
