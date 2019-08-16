"""
@author: acfromspace
"""


def designer_door_mat(rows, columns):
    # Print
    for index in range(1, rows, 2):
        print((index * ".|.").center(columns, "-"))

    # Print "WELCOME" in the center surrounded by "-" till there's a total of `len(column)`
    print("WELCOME".center(columns, "-"))

    for index in range(rows-2, -1, -2):
        print((index * ".|.").center(columns, "-"))


print("Please input rows and columns:")
rows, columns = map(int, input().split())
designer_door_mat(rows, columns)
