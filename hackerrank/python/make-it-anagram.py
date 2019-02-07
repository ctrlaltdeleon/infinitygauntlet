"""
@author: acfromspace
"""

w1 = input()
w2 = input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    # abs = absolute number, because we don't want negative character deletions
    # count = returns amount of object occurs in the list
    total += abs(w1.count(letter) - w2.count(letter))
print(total) # total number of character deletions

"""
For example:
w1 = abc
w2 = cde

a, b, d, e are taken out, 4 character deletions
c remains there, not deleted, because:
total += abs(w1.count(letter) - w2.count(letter))
0 += absolute value of(w1."once"(c) - w2."once"(c))
"""