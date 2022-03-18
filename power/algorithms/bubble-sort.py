"""
Best time complexity: O(n)
Worst time complexity: O(n^2)
Best space complexity: O(1)
Worst space complexity: O(1)
"""

def bubble_sort_1(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def bubble_sort_2(data):
    # %last_index% is here to keep check of amount of passes, not needed for bubble sort.
    last_index = len(data) - 1
    # Checks last step to see if it was the last needed step.
    # (len(data) - last_index) is number of passes when it's sorted.
    is_sorted = False
    while last_index > 0 and not is_sorted:
        for i in range(last_index):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = False
            else:
                is_sorted = True
        last_index -= 1
    return data

def bubble_sort_3(data):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                is_sorted = False
    return data

test_list_1 = [9, 5, 1, 3, 6, -2, -8]
test_list_2 = [9, 5, 1, 3, 6, -2, -8]
print("bubble_sort_1():", test_list_1, "=>", bubble_sort_1(test_list_2))
test_list_1 = [9, 5, 1, 3, 6, -2, -8]
test_list_2 = [9, 5, 1, 3, 6, -2, -8]
print("bubble_sort_2():", test_list_1, "=>", bubble_sort_2(test_list_2))
test_list_1 = [9, 5, 1, 3, 6, -2, -8]
test_list_2 = [9, 5, 1, 3, 6, -2, -8]
print("bubble_sort_3():", test_list_1, "=>", bubble_sort_3(test_list_2))

"""
bubble_sort_1(): [9, 5, 1, 3, 6, -2, -8] => [-8, -2, 1, 3, 5, 6, 9]
bubble_sort_2(): [9, 5, 1, 3, 6, -2, -8] => [-8, -2, 1, 3, 5, 6, 9]
bubble_sort_3(): [9, 5, 1, 3, 6, -2, -8] => [-8, -2, 1, 3, 5, 6, 9]
"""