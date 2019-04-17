"""
@author: acfromspace
"""

"""
DESCRIPTION:

A colony of 8 cells are next to each other.
Each day, for each cell, if its neighbors are both active or both inactive, the cell becomes active else inactive.
Assume there are cells next to the end points that are not seen.
 
SAMPLE INPUT 1:

[1,0,0,0,0,1,0,0],1
 
SAMPLE OUTPUT 1:

[0,1,0,0,1,0,1,0]

SAMPLE INPUT 2:

[1,1,1,0,1,1,1,1,],2
 
SAMPLE OUTPUT 2:

[0,0,0,0,0,1,1,0]
"""


def cell_compete(cells, days):
    for index in range(days):
        copy_cells = []
        for index in range(1, 9):
            copy_cells.append(cells[index-1])
        copy_cells.insert(0, 0)
        copy_cells.append(0)
        for index in range(8):
            if copy_cells[index] is copy_cells[index+2]:
                cells[index] = 0
            else:
                cells[index] = 1
    return cells


list1 = [1, 0, 0, 0, 0, 1, 0, 0]
list2 = [1, 1, 1, 0, 1, 1, 1, 1]
cell_compete(list1, 1)
cell_compete(list2, 2)
print("cell_compete(list1, 1):", list1)
print("cell_compete(list2, 2):", list2)
