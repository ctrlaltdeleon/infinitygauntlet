def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        return dec_to_bin(number // 2) + dec_to_bin(number % 2)

number = int(input("Input a decimal number: "))
print("dec_to_bin():", dec_to_bin(number))

"""
Input a decimal number: 21
dec_to_bin(): 10101
"""

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