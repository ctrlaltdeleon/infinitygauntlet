"""
@author: acfromspace
"""

import random
import time


def inorder(data):
    for index in range(len(data)-1):
        if data[index] > data[index + 1]:
            return False
    return True


def bogo(data):
    while not inorder(data):
        random.shuffle(data)
    return data


random.seed()
data = []
for i in range(0, 10):
    data.append(random.randrange(0, 100))
start = time.time()
print("Before: ", data)
data = bogo(data)
print("After: ", data)
print("Sort took %.2f seconds" % (time.time() - start))
