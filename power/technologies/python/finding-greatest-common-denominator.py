
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


def finding_greatest_common_denominator(data, size):
    a = data[0]
    b = data[1]
    result = gcd(a, b)
    for index in range(2, size):
        result = gcd(result, data[index])
    return result


list1 = [4, 8, 16, 32]
print("finding_greatest_common_denominator():",
      finding_greatest_common_denominator(list1, len(list1)))
