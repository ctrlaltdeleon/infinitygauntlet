"""
@author: acfromspace
"""

# class Range(object):
#     def __init__(self):
#         self.lower_bound = -1
#         self.upper_bound = -1

#     def __init__(self, lower_bound, upper_bound):
#         self.lower_bound = lower_bound
#         self.upper_bound = upper_bound

#     def __str__(self):
#         return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"


# def merge_integer_ranges(input_range_list):
#     if (input_range_list == None or len(input_range_list) <= 1):
#         return input_range_list
#     output_list = []
#     previous = input_range_list[0]
#     index = 1
#     while index < len(input_range_list):
#         current = input_range_list[index]
#         if (previous.upper_bound >= current.lower_bound):
#             merged = Range(previous.lower_bound, max(
#                 previous.upper_bound, current.upper_bound))
#             previous = merged
#         else:
#             output_list.append(previous)
#             previous = current
#         index = index + 1

#     output_list.append(previous)
#     return output_list


# input_range_list = [[1, 10], [5, 8], [8, 15]]
# print("merge_integer_ranges():", merge_integer_ranges(input_range_list))
