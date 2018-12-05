"""
Created 3/3/2018

@author: acfromspace
"""


def intDivision(a, b):
    return a // b


def floatDivision(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(intDivision(a, b), floatDivision(a, b), sep="\n")
