#include <iostream>
using namespace std;

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