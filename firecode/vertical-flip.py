"""
@author: acfromspace
"""


def flip_vertical_axis(matrix):

    change = []

    for row in matrix:
        change.append(row[::-1])
    return change


matrix = [[0, 1], [0, 2]]
print(flip_vertical_axis(matrix))
