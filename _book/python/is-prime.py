"""
@author: acfromspace
"""


def isPrime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


number = int(input("Input a number to check if prime: "))
print("isPrime():", isPrime(number))
