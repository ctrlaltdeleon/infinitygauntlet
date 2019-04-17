"""
@author: acfromspace
"""


def better_fibonacci(n):
    n1, n2 = 0, 1
    for index in range(n):
        n1, n2 = n2, n1 + n2
    return n1


n = int(input("Input an integer: "))
print("better_fibonacci():", better_fibonacci(n))
