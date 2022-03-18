def fib_1(number):
    if number < 2:
        return number
    else:
        return fib_1(number-1) + fib_1(number-2)


def fib_2(number):
    if number < 2:
        return number
    prev = 0
    curr = 1
    for index in range(2, number):
        curr, prev = curr+prev, curr
    return curr+prev

number = int(input("Input the fibonacci sequence end amount: "))
print("Recursive form, fib_1():", fib_1(number))
print("Iterative form, fib_2():", fib_2(number))

"""
Input the fibonacci sequence end amount: 10
Recursive form, fib_1(): 55
Iterative form, fib_2(): 55
"""