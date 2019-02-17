"""
@author: acfromspace
"""

import math


class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):

    # O(sqrt(n)) complexity since it doesn't have to go through most of the higher numbers besides itself
    def divisorSum(self, n):
        sum = 0
        for index in range(1, int(math.sqrt(n)+1)):
            if n % index == 0:
                first, second = index, n/index
                sum += first
                if first != second:
                    sum += second
        return int(sum)


"""
    def divisorSum(self, n):
        sum = 0
        for index in range(1, n+1):
            if n % index == 0:
                sum += index
        return sum
"""

n = int(input("Input a number to find sum of non-remainder divisible: "))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
