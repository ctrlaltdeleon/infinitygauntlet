"""
@author: acfromspace
"""

#!/bin/python3

import sys


def isBad(S):

    try:
        print(int(S))
    except:
        print("Bad String")


if __name__ == "__main__":

    S = input("Input: ").strip()

    isBad(S)

"""
First try w/o knowing exception handles:

integer = int(S)

if integer is not None:
    print(integer)
else:
    print("Bad String")
"""

"""
NOTE: Hackerrank has a weird time compiling, needs to be strict w/o comments and with exception handles
Accepted answer on Hackerrank:

S = input().strip()

try:
    print(int(S))
except:
    print("Bad String")
"""
