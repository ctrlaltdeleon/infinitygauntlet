"""
@author: acfromspace
"""


def staircase1(n):
    for index in range(1, n+1):
        soln = ""
        spaces = n - index
        stair = index
        for index in range(spaces):
            soln += " "
        for index in range(stair):
            soln += "#"
        print(soln)


def staircase2(n):
    for index in range(1, n+1):
        print(" "*(n-index) + "#"*(index))


staircase1(4)
staircase1(6)
staircase1(10)
staircase2(4)
staircase2(6)
staircase2(10)
