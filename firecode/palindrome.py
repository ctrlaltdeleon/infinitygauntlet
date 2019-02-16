"""
@author: acfromspace
"""


def is_palindrome(input_string):
    return input_string == input_string[::-1]


input_string = "racecar"
print(is_palindrome(input_string))
