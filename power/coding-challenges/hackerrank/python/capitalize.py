"""
@author: acfromspace
"""


def capitalize(s):
    return " ".join(map(str.capitalize, s.split(" ")))


s = "1 2 hi hello noPE 12re w"
print("capitalize():", capitalize(s))
