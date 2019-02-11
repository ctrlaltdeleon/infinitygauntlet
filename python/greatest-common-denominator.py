"""
DESCRIPTION:

A list of numbers are given.
Find the greatest commmon denominator amongst them.
 
SAMPLE INPUT 1:

[12, 36, 60]
 
SAMPLE OUTPUT 1:

12

SAMPLE INPUT 2:

[20, 28]
 
SAMPLE OUTPUT 2:

24
"""


def gcd(a, b):

    while(b):
        a, b = b, a % b

    return a


def findingGCD(data, size):

    a = data[0]
    b = data[1]
    result = gcd(a, b)

    for counter in range(2, size):
        result = gcd(result, data[counter])

    return result


if __name__ == "__main__":

    list1 = [4, 8, 16, 32]

    print(findingGCD(list1, len(list1)))
