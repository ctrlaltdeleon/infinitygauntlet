#include <iostream>
using namespace std;

int main()
{
    int n;
    string num[10] = {"Greater than 9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> "Input a number to be translated to text: " >> n;

    // cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (n > 9)
    {
        cout << num[0];
    }
    else if
    {
        cout << num[n];
    }
    else
    {
        cout << "Out of bounds!"
    }

    return 0;
}