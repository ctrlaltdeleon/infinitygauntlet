

import random
import time


def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True


def bogo(x):
    while not inorder(x):
        random.shuffle(x)
    return x


random.seed()
x = []
for i in range(0, 10):
    x.append(random.randrange(0, 100))
start = time.time()
print("Before: ", x)
x = bogo(x)
print("After: ", x)
print("%.2f seconds" % (time.time() - start))
