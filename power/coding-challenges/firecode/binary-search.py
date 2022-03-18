def binary_search(a_list, item):
    left = 0
    right = len(a_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if a_list[mid] == item:
            return True
        elif a_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return False

a_list = [0, 2, 4, 8]
item = 8
print("binary_search():", binary_search(a_list, item))

"""
binary_search(): True
"""