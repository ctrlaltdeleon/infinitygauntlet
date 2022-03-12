"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def counting_valleys(n, s):
    inValley = False
    vallies = 0
    height = 0
    for step in s:
        if step == 'U':
            height += 1
        else:
            height -= 1
        if not inValley:
            if height < 0:
                inValley = True
        elif height == 0:
            inValley = False
            vallies += 1
    return vallies


n = int(input("Input number of steps taken: "))
s = input("""Input string "U" and "D" to create a path: """)
print("counting_valleys():", counting_valleys(n, s))
