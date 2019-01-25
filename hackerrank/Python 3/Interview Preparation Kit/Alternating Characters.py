"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):

    deletions = 0

    for counter, character in enumerate(s[:-1]):
        # if the character at this index is == to the character we're seeing now
        # character == s[counter]
        if s[counter+1] == character:
            deletions += 1

    # # this stops at the first encounter, doesn't loop
    # if any(s[counter+1] == character for counter, character in enumerate(s[:-1])):
    #     deletions += 1

    return deletions


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Input number of strings: "))

    for q_itr in range(q):
        s = input("Input string %i: " % (q_itr+1))

        print("Answer:", alternatingCharacters(s))

        # result = alternatingCharacters(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
