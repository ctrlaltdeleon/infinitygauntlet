"""
@author: acfromspace
"""


def isPower1(number):
    power = 4
    if (number <= 0):
        return False
    while (number != 1):
        if (number % power != 0):
            return False
        number = number // power
    return True


def isPower2(number, base):
    while (number % base == 0):
        number = number / base
    # this says if the number given after many divisions is 1, return true
    return number == 1


"""
Determine if the number creates true base^power
power = power being found
base = any number that satisfies
"""

number = 64
base = 2
print(isPower1(number))
print(isPower2(number, base))
