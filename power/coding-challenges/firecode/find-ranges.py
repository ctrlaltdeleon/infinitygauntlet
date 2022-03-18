def find_range(input_list, input_number):
    search = []
    number_range = []
    for index in range(1, len(input_list)):
        if input_list[index] == input_number:
            search.append(index)
        if input_list[index] > input_number:
            break
    number_range.append(search[0])
    number_range.append(search[-1])
    return number_range

input_list = [1, 2, 5, 5, 8, 8, 10, 8]
input_number = 8
print("find_range():", find_range(input_list, input_number))
input_number = 2
print("find_range():", find_range(input_list, input_number))

"""
find_range(): [4, 5]
find_range(): [1, 1]
"""