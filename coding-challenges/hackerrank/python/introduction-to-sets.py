"""
@author: acfromspace
"""


def average(array):
    return sum(set(array)) / len(set(array))


array = [100, 200, 100, 300, 200, 400, 500, 600, 200]
print("average():", average(array))
