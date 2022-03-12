"""
@author: acfromspace
"""


def make_palindrome(string):
    if string == string[::-1]:
        return string
    else:
        back = string[::-1]
        back = back[1:]
        return string + back


string = str(input("Input a string to make a palindrome: "))
print("make_palindrome():", make_palindrome(string))

"""
Pythonic solution:

Great use of recursion here:
    def make_palindrome(string):
        if string == string[::-1]:
            return string
        else:
            return string[0] + make_palindrome(string[1:]) + string[0]

race
r
a
c
e
c
a
r
"""
