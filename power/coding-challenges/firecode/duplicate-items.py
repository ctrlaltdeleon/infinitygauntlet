"""
@author: acfromspace
"""


def duplicate_items(list_numbers):
    duplicates = []
    list_numbers.sort()
    for index in range(1, len(list_numbers)):
        # If the number we look at is equal to the number before, we append it.
        if list_numbers[index] is list_numbers[index - 1]:
            duplicates.append(list_numbers[index])
    # This cuts down unnecessary truths.
    return list(set(duplicates))


list_numbers = [1, 2, 3, 2, 4, 5, 1, 2]
print("duplicate_items():", duplicate_items(list_numbers))

"""
Pythonic solution:
def duplicate_items(list_numbers):
    set_list = set(list_numbers)
    return [i for i in set_list if list_numbers.count(i)>1]
"""
