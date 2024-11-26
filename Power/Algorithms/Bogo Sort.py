"""
Best time complexity: O(n)
Worst time complexity: Unbounded
Best space complexity: O(1)
Worst space complexity: O(1)
"""

import random
import time

def in_order(data):
    for index in range(len(data)-1):
        if data[index] > data[index + 1]:
            return False
    return True

# Also known as stupid sort, sorts randomly and checks if it's in order.
def bogo(data):
    while not in_order(data):
        random.shuffle(data)
    return data

random.seed()
data = []
for i in range(0, 10):
    data.append(random.randrange(0, 100))
start = time.time()
print("Before:", data)
data = bogo(data)
print("After:", data)
print("Sort took %.2f seconds" % (time.time() - start))

"""
Before: [66, 79, 79, 69, 64, 26, 74, 44, 74, 52]
After: [26, 44, 52, 64, 66, 69, 74, 74, 79, 79]
Sort took 8.07 seconds
"""