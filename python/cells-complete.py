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


def cellCompete(cells, days):

    for counter in range(days):
        copy_cells = []
        for counter in range(1, 9):
            copy_cells.append(cells[counter-1])

        copy_cells.insert(0, 0)
        copy_cells.append(0)

        for counter in range(8):
            if copy_cells[counter] is copy_cells[counter+2]:
                cells[counter] = 0
            else:
                cells[counter] = 1

    return cells


if __name__ == "__main__":

    list1 = [1, 0, 0, 0, 0, 1, 0, 0]
    list2 = [1, 1, 1, 0, 1, 1, 1, 1]

    cellCompete(list1, 1)
    cellCompete(list2, 2)

    print(list1)
    print(list2)
