from collections import Counter

def make_anagram(a, b):
    a = Counter(a)
    a.subtract(Counter(b))
    return sum(map(abs, a.values()))

a = input("Input string 1: ")
b = input("Input string 2: ")
print("make_anagram():", make_anagram(a, b))

"""
Input string 1: hello
Input string 2: there
make_anagram(): 6
"""

"""
INPUT:
a = abc
b = cde

OUTPUT:
4

EXPLANATION:
4 deletions needed with "c" remaining.
"""