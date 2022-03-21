

def allFib(n):
    for index in range(n):
        print(index+1, ":", fib(index))


def fib(n):
    if (n <= 0):
        return 0
    if (n == 1):
        return 1
    return fib(n-1) + fib(n-2)


n = 10
allFib(n)
