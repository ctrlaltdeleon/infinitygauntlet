/*
DESCRIPTION:

Write a program to count each occurrence of each letter and number in a string.
Keep upper case and lower case letters separate.
Start your program by declaring a character array, msg, with a size of 120 or greater.

char msg[MAX];

The user should then type a text string into the array:

cin.getline(msg, MAX);

Then, using FUNCTION, count and display the number of times each letter and number appear.
You may wish to consult an ASCII chart to help you out.
*/

#include <iostream>
#include <iomanip>

using namespace std;

// Global.
    const int MSG_MAX = 120;
    const int LETTERS_MAX = 26;
    const int NUMBERS_MAX = 10;

// Prototypes.
    void function(char msg[], int lowerLetters[], int upperLetters[], int numbers[]);
    void betterFunction(char msg[], int maximum, int check[], char startingPoint);

int main()
{
    // Declarations.
    char msg[MSG_MAX] = {0};
    int lowerLetters[LETTERS_MAX] = {0};
    int upperLetters[LETTERS_MAX] = {0};
    int numbers[NUMBERS_MAX] = {0};

    // Get "string" from users.
    array:cin.getline(msg, MSG_MAX);

    // function(msg, lowerLetters, upperLetters, numbers);
    betterFunction(msg, LETTERS_MAX, lowerLetters, 'a');
    betterFunction(msg, LETTERS_MAX, upperLetters, 'A');
    betterFunction(msg, NUMBERS_MAX, numbers, '0');

    cout << "Hello!";

    return 0;
}

void function(char msg[], int lowerLetters[], int upperLetters[], int numbers[])
{
    for (int i = 0; i < LETTERS_MAX; i++) // LOWER Alphabet.
    {
        for (int j = 0; j < MSG_MAX; j++) // String.
        {
            if (msg[j] == static_cast<char>(i+'a')) lowerLetters[i]++;
        }
        cout << static_cast<char>(i + 'a') << " - " << lowerLetters[i] << endl;
    }

    for (int i = 0; i < LETTERS_MAX; i++) // UPPER Alphabet.
    {
        for (int j = 0; j < MSG_MAX; j++) // String.
        {
            if (msg[j] == static_cast<char>(i + 'A')) upperLetters[i]++;
        }
        cout << static_cast<char>(i + 'A') << " - " << upperLetters[i] << endl;
    }

    for (int i = 0; i < NUMBERS_MAX; i++) // Numbers.
    {
        for (int j = 0; j < MSG_MAX; j++) // String.
        {
            if (msg[j] == static_cast<char>(i + '0')) numbers[i]++;
        }
        cout << static_cast<char>(i + '0') << " - " << numbers[i] << endl;
    }
}


void betterFunction(char msg[], int maximum, int check[], char startingPoint)
{
    for (int i = 0; i < maximum; i++)
    {
        for (int j = 0; j < MSG_MAX; j++) // String.
        {
            if (msg[j] == static_cast<char>(i + startingPoint)) check[i]++;
        }
        cout << static_cast<char>(i + startingPoint) << " - " << check[i] << endl;
    }
}

/*
You have dogs? I have 123 dogs.
a - 2
b - 0
c - 0
d - 2
e - 2
f - 0
g - 2
h - 2
i - 0
j - 0
k - 0
l - 0
m - 0
n - 0
o - 3
p - 0
q - 0
r - 0
s - 2
t - 0
u - 1
v - 2
w - 0
x - 0
y - 0
z - 0
A - 0
B - 0
C - 0
D - 0
E - 0
F - 0
G - 0
H - 0
I - 1
J - 0
K - 0
L - 0
M - 0
N - 0
O - 0
P - 0
Q - 0
R - 0
S - 0
T - 0
U - 0
V - 0
W - 0
X - 0
Y - 1
Z - 0
0 - 0
1 - 1
2 - 1
3 - 1
4 - 0
5 - 0
6 - 0
7 - 0
8 - 0
9 - 0
Hello!
*/