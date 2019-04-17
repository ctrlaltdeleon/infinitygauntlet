"""
@author: acfromspace
"""

"""
base^power = number
base = any number that satisfies
power = power being found
number = product
"""


def is_power_1(number):
    power = 4
    if (number <= 0):
        return False
    while (number != 1):
        if (number % power != 0):
            return False
        number = number // power
    return True


def is_power_2(number, base):
    while (number % base == 0):
        number = number / base
    return number == 1


number = 64
base = 2
print("is_power_1():", is_power_1(number))
print("is_power_2():", is_power_2(number, base))
