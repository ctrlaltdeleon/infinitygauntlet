n = int(input("Enter a number and print all odd numbers less than it: "))

def print_odd(n):
    for index in range(n+1):
        if index % 2 != 0:
            print(index)

print_odd(n)

"""
Enter a number and print all odd numbers less than it: 20
1
3
5
7
9
11
13
15
17
19
"""