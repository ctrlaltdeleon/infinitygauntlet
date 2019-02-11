#include <iostream>
using namespace std;

/*
DESCRIPTION:

A list of numbers are given.
Find the greatest commmon denominator amongst them.
 
SAMPLE INPUT 1:

[12, 36, 60]
 
SAMPLE OUTPUT 1:

12

SAMPLE INPUT 2:

[20, 28]
 
SAMPLE OUTPUT 2:

24
*/

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return (b % a, a);
}

int findingGCD(int *arr, int len)
{
    int result = arr[0];
    for (int counter = 1; counter < len; counter++)
    {
        result = gcd(arr[counter], result);
    }
    return result;
}

int main()
{
    int arr[] = {2, 3, 5, 6, 10, 15, 30};
    int len = sizeof(arr) / sizeof(arr[0]);
    cout << findingGCD(arr, len) << endl;
    return 0;
}