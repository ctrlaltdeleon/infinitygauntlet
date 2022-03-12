"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys
from collections import Counter


def make_anagram(a, b):
    a = Counter(a)
    a.subtract(Counter(b))
    return sum(map(abs, a.values()))


a = input("Input string 1: ")
b = input("Input string 2: ")
print("make_anagram():", make_anagram(a, b))

"""
INPUT:
a = abc
b = cde

OUTPUT:
4

EXPLANATION:
4 deletions needed with "c" remaining.
"""
