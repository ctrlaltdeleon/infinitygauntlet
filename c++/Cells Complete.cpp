#include <iostream>
using namespace std;

int *cellCompete(int *cells, int days)
{
    for (int counter = 0; counter < days; counter++)
    {
        int data_cells[10];
        for (int counter = 1; counter < 9; counter++)
        {
            data_cells[counter] = cells[counter - 1];
        }

        data_cells[0] = 0;
        data_cells[9] = 0;

        for (int counter = 0; counter < 8; counter++)
        {
            cells[counter] = data_cells[counter] == data_cells[counter + 2] ? 0 : 1;
        }
    }
    return cells;
}

int main()
{
    int arr[8] = {1, 1, 1, 0, 1, 1, 1, 1};
    int arr2[8] = {1, 0, 0, 0, 0, 1, 0, 0};

    cellCompete(arr2, 1);

    for (int counter = 0; counter < 8; counter++)
    {
        cout << arr2[counter] << " ";
    }
}