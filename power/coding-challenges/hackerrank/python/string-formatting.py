def print_formatted(number):
    width = len(str(bin(number)))-2
    for num in range(1, number+1):
        decimal = int(num)
        octal = oct(num)
        hexadecimal = hex(num)
        binary = bin(num)
        print(str(decimal).rjust(width), octal[2:].rjust(
            width), hexadecimal[2:].title().rjust(width), binary[2:].rjust(width))

print_formatted(20)

"""
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
   18    22    12 10010
   19    23    13 10011
   20    24    14 10100
"""