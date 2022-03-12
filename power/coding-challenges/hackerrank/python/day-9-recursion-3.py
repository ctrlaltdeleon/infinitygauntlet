"""
@author: acfromspace
"""

import math
import os
import random
import re
import sys


def factorial(n):
    # Python has it's own factorial library as well
    # math.factorial(input())
    return 1 if n <= 1 else n * factorial(n-1)


n = int(input("Input a number to factorial(n): "))
result = factorial(n)
print("The answer is:", result)
