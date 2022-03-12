"""
@author: acfromspace
"""

from collections import Counter


def mostCommonElements(data):
    # Parameter for `most_common()` is to provide how many of the most common elements.
    return [index[0] for index in Counter(data).most_common(3)]


data = [1, 2, 3, 3, 2, 2, 1, 1, 1, 9, 9, 9, 9]
print(mostCommonElements(data))
