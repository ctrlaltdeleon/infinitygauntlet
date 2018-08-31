/*
Created 5/19/2018

@author: acfromspace
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solveMeFirst(int a, int b) {
 return a + b;
}

int main() {
  int num1, num2;
  int sum;
  // Takes the first two numbers separated by new lines  
  cin >> num1 >> num2;
  sum = solveMeFirst(num1,num2);
  cout << sum;
  return 0;
}