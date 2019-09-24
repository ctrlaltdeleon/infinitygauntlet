"""
@author:acfromspace
"""


def smallest(list1):
    smallest = list1[0]
    for index in list1:
        if index < smallest:
            smallest = index
    return smallest


list1 = [5, 2, 2, 3, 4, 5, 9, 0, 1, 8]
print("smallest():", smallest(list1))

# Time Complexity? O(n)
# Any way to be faster? For an unsorted array, no.
