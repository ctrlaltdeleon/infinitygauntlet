"""
@author: acfromspace
"""

def loop(test_number):
    for counter in range(0, test_number):
        print(squared(counter))

def squared(test_number):
    return test_number ** 2

if __name__ == '__main__':
    n = int(input())

    loop(n)