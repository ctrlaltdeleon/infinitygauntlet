"""
@author: acfromspace
"""

import math


class AdvancedArithmetic(object):
    def divisor_sum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    # O(sqrt(n)) complexity since it doesn't have to go through most of the higher numbers besides itself.
    def divisor_sum(self, n):
        sum = 0
        for index in range(1, int(math.sqrt(n)+1)):
            if n % index == 0:
                sum += index
                if index != n/index:
                    sum += n/index
        return int(sum)


n = int(input("Input a number to find sum of non-remainder divisible: "))
my_calculator = Calculator()
s = my_calculator.divisor_sum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

"""
Pythonic solution:
    sum(list(filter(lambda x: n % x == 0, [x for x in range(1, n+1)])))
"""
