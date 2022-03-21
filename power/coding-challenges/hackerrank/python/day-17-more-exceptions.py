class Calculator:
    def power(self, n, p):
        # Assert says "if this statement is true, throw this exception".
        # Used to detect problems early in the program, like a "if break".
        assert n >= 0 and p >= 0, "n and p should be non-negative"
        return n ** p

myCalculator = Calculator()
T = int(input("Input number of trials: "))
for i in range(T):
    n, p = map(int, input("Input two integers: ").split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

"""
Input number of trials: 3
Input two integers: 2 5
32
Input two integers: 1 10
1
Input two integers: 3 3
27
"""