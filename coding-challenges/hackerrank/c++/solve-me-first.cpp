/*
@author: acfromspace
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solve_me_first(int a, int b)
{
	return a + b;
}

int main()
{
	int num1, num2, sum;
	cin >> num1 >> num2;
	sum = solve_me_first(num1, num2);
	cout << sum;
	return 0;
}