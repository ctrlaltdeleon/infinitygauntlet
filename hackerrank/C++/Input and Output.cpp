/*
@author: acfromspace
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a, b, c, together;

    // Figure a better way to do input validation for integers only from numbers 0 to 1000
    cin >> a >> b >> c;

    together = a + b + c;

    cout << together;

    return 0;
}
