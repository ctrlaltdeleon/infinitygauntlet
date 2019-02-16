"""
@author: acfromspace
"""


def dec_to_bin(n):

    if n < 2:
        return str(n)
    else:
        return dec_to_bin(n//2) + dec_to_bin(n % 2)


"""
INPUT:
21

FUNCTION:
21
21 // 2 = 10
    10 // 2 = 5
        5 // 2 = 2
            2 // 2 = 1 --> return 1
            2 % 2 = 0 --> return 0
        5 % 2 = 1 --> return 1
    10 % 2 = 0 --> return 0
21 % 2 = 1 --> return 1

OUTPUT:
10101

INPUT:
13

FUNCTION:
13
13 // 2 = 6
    6 // 2 = 3
        3 // 2 = 1 --> return 1
        3 % 2 = 1 --> return 1
    6 % 2 = 0 --> return 0
13 % 2 = 1 --> return 1

OUTPUT:
1101
"""

if __name__ == "__main__":

    n = int(input("Input a decimal number: "))
    print(dec_to_bin(n))
