"""
@author: acfromspace
"""

# Recursive form


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Iterative form


def fib2(n):
    if n < 2:
        return n
    prev = 0
    curr = 1
    for index in range(2, n):
        curr, prev = curr+prev, curr
    return curr+prev


n = int(input("Input the fibonacci sequence end amount: "))
print(fib(n))
print(fib2(n))
