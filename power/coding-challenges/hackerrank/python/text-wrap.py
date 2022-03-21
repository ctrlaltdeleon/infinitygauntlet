import textwrap

def wrap1(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

def wrap2(string, max_width):
    return textwrap.fill(string, max_width)

def wrap3(string, max_width):
    # Doesn't work as a solution to the problem, but brings easier reading to the answer.
    for index in range(0, len(string), max_width):
        print(string[index:index+max_width])

string, max_width = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4
print("wrap1():", wrap1(string, max_width))
print("wrap2():", wrap2(string, max_width))
print("wrap3():")
wrap3(string, max_width)

"""
wrap1(): ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
wrap2(): ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
wrap3():
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
"""