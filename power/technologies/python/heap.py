"""
@author: acfromspace
"""

import heapq

li = [5, 7, 9, 1, 3]
print("The initial list is:", li)

# Using `heapify` to convert list into a min-heap.
# For a max-heap use `_heapify_max`.
heapq.heapify(li)

# Printing created min-heap.
print("The created min-heap is:", li)

# Using `heappush()` to push elements into heap.
heapq.heappush(li, 4)
print("The modified heap after push is:", li)

print("The popped and smallest element is:", heapq.heappop(li))

print("The modified heap after pop is:", li)
