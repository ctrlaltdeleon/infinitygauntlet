/*
@author: acfromspace
*/

#include <iostream>
using namespace std;

/*
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
*/

int *cell_compete(int *cells, int days)
{
    for (int index = 0; index < days; index++)
    {
        int data_cells[10];
        for (int index = 1; index < 9; index++)
        {
            data_cells[index] = cells[index - 1];
        }

        data_cells[0] = 0;
        data_cells[9] = 0;

        for (int index = 0; index < 8; index++)
        {
            cells[index] = data_cells[index] == data_cells[index + 2] ? 0 : 1;
        }
    }
    return cells;
}

int main()
{
    int arr[8] = {1, 1, 1, 0, 1, 1, 1, 1};
    int arr2[8] = {1, 0, 0, 0, 0, 1, 0, 0};

    cell_compete(arr2, 1);

    for (int index = 0; index < 8; index++)
    {
        cout << arr2[index] << " ";
    }
}