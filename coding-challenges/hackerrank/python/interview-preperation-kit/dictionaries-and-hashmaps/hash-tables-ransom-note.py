"""
@author: acfromspace
"""


import math
import os
import random
import re
import sys
from collections import Counter


def check_magazine(magazine, note):
    if (Counter(note) - Counter(magazine)) != {}:
        return print("No")
    return print("Yes")


magazine = input("Insert words available in magazine: ").rstrip().split()
note = input("Insert ransom note: ").rstrip().split()
print("check_magazine():", check_magazine(magazine, note))
