"""
@author: acfromspace
"""


def factorial(number):
    solution = 1
    for index in range(1, number+1):
        solution *= index
    return solution


def factorialRecursion(number):
    # Think about it if `number` = 3, then it will compute as 3 * 2 * 1.
    return number if number <= 1 else factorialRecursion(number-1) * number


number = 5
print("factorial():", factorial(number))
print("factorialRecursion():", factorialRecursion(number))
