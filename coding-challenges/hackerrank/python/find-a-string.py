"""
@author: acfromspace
"""


def count_substring(string, sub_string):
    count = 0
    for index in range(len(string)):
        if string[index:].startswith(sub_string):
            count += 1
    return count


print("count_substring():", count_substring("ABCDEFEFE", "EFE"))
