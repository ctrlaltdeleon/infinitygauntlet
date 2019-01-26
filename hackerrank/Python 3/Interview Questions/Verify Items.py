"""
@author: acfromspace
"""

"""
return an INT
origItems = string array
origPrices = float array
items = string array
prices = float array
"""


def verifyItems(origItems, origPrices, items, prices):
    # Write your code here

    incorrect = 0

    original = dict(zip(origItems, origPrices))
    michael = dict(zip(items, prices))

    # this only compares values though, not taking into account
    for counter in michael.items():
        if counter not in original.items():
            incorrect += 1

    return incorrect
