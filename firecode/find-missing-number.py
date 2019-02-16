"""
@author: acfromspace
"""


def find_missing_number(list_numbers):

    for key, value in enumerate(list_numbers, start=1):
        if key != value:
            return key

# Assuming the list is sorted with no gaps
# Checks "is key equal to the value? if not, that's the missing value" In this case "key" means "index"


list_numbers = [1, 2, 3, 5, 6, 7, 8, 9]
print(find_missing_number(list_numbers))
