"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):

    # Note: Python has it's own factorial library as well
        # math.factorial(input())
    return 1 if n <= 1 else n * factorial(n-1)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Input a number to factorial(n): "))

    result = factorial(n)

    print("The answer is:", result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
