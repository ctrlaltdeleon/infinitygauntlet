"""
@author: acfromspace
"""


def populateArray(col, row):
    square = []
    for colNum in range(col):
        square.append([])
        for rowNum in range(row):
            coordinates = str(colNum) + "," + str(rowNum)
            square[colNum].append(coordinates)
    return square


col = 4
row = 4
print("populateArray():", populateArray(col, row))
