"""
@author: acfromspace
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):

    # Counter library provides fast data collection to compare both at the same time
    # if an empty dict is returned, that means the ransom note can be created, otherwise, no
    if (Counter(note) - Counter(magazine)) != {}:
        return print("No")

    return print("Yes")

    # initial solution that works, but when scaled, takes a while
    # for words in note:
    #     if words not in magazine:
    #         return print("No")
    #     else:
    #         # used for duplicates
    #         magazine.remove(words)

    # return print("Yes")


if __name__ == '__main__':
    mn = input("Insert number values for m (magazine) and n (note): ").split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input("Insert words available in magazine: ").rstrip().split()

    note = input("Insert ransom note: ").rstrip().split()

    checkMagazine(magazine, note)
