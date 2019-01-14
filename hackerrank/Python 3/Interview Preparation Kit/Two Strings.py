"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):

    return 'YES' if any(substring in s1 for substring in s2) else 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Number of comparisons to be done: "))

    for q_itr in range(q):
        s1 = input("String 1 in iteration %i: " % (q_itr + 1))

        s2 = input("String 2 in iteration %i: " % (q_itr + 1))

        print("Is there a commonality between the two strings?", twoStrings(s1, s2))

        # result = twoStrings(s1, s2)

    # fptr.write(result + '\n')

    # fptr.close()
