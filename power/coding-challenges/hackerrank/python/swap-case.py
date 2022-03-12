"""
@author: acfromspace
"""


def swap_case1(s):
    solution = []
    for index in s:
        if index.isupper() == True:
            solution.append(index.lower())
        elif index.islower() == True:
            solution.append(index.upper())
        else:
            solution.append(index)
    return "".join(solution)


def swap_case2(s):
    return "".join([i.lower() if i.isupper() else i.upper() for i in s])


def swap_case3(s):
    return s.swapcase()


print("swap_case1(s):", swap_case1("joji JOJI"))
print("swap_case2(s):", swap_case2("joji JOJI"))
print("swap_case3(s):", swap_case3("joji JOJI"))
