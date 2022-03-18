def kangaroo(x1, v1, x2, v2):
    if v2 >= v1 and x2 >= x1:
        return "NO"
    elif (x1 - x2) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = map(int, input(
    "Input start distance #1, jump distance #1, start distance #2, jump distance #2: ").split())
print("kangaroo():", kangaroo(x1, v1, x2, v2))

"""
Input start distance #1, jump distance #1, start distance #2, jump distance #2: 1 3 1 4
kangaroo(): NO
"""