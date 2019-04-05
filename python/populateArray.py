"""
@author: acfromspace
"""


def populateArray(col, row):
    coolSquare = []
    for colNum in range(col):
        coolSquare.append([])
        for rowNum in range(row):
            nice = str(colNum) + "," + str(rowNum)
            coolSquare[colNum].append(nice)
    return coolSquare


col = 4
row = 4
print("populateArray():", populateArray(col, row))
