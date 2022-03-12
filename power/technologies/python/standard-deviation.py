"""
@author: acfromspace
"""

import statistics


def standardDeviation(array):
    return statistics.stdev(array)


array = [0.8, 0.4, 1.2, 3.7, 2.6, 5.8]
print("standardDeviation():", standardDeviation(array))
