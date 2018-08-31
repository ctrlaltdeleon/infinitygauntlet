"""
Created 3/6/2018

@author: acfromspace
"""

def printSingleLine(n):
    # * unpacks the list
    print(*range(1, n + 1), sep='')

if __name__ == '__main__':
    n = int(input())
    
    printSingleLine(n)