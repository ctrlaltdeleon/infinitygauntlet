def factorial(n):
    # Python has it's own factorial library as well
    # import math, math.factorial(input())
    return 1 if n <= 1 else n * factorial(n-1)

n = int(input("Input a number to factorial(n): "))
result = factorial(n)
print("The answer is:", result)

"""
Input a number to factorial(n): 3
The answer is: 6
"""