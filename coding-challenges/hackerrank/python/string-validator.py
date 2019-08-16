"""
@author: acfromspace
"""


def string_validator(s):
    print(any(index.isalnum() for index in s))
    print(any(index.isalpha() for index in s))
    print(any(index.isdigit() for index in s))
    print(any(index.islower() for index in s))
    print(any(index.isupper() for index in s))


s = "joji2"
string_validator(s)
