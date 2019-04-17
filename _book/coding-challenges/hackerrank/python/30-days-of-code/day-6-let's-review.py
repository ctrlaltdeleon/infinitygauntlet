"""
@author: acfromspace
"""

if __name__ == "__main__":

    test_cases = int(input("Number of test cases: "))
    for counter in range(test_cases):
        even, odd = "", ""
        string = input("Input the string to divide even and odd indexes by: ")
        for counter, value in enumerate(string):
            if counter % 2 == 0:
                even += value
            else:
                odd += value
        print(even, odd)


"""
Pythonic solution:
    for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])

To elaborate, print(even, odd):
Join to empty string every even number starting with 0.
Join to empty string every odd number starting with 1.
    print(*["".join(string[::2]), "".join(string[1::2])])
"""
