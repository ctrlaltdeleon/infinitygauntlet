"""
@author: acfromspace
"""

def isEven(test_number):
    return test_number % 2 == 0

def inDefinedLimit(test_number):
    return test_number in range(2, 6) or test_number > 20
    # Defined limit is between 2 to 6 or greater than 20

if __name__ == '__main__':
    n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}

    print(check[isEven(n) and inDefinedLimit(n)])