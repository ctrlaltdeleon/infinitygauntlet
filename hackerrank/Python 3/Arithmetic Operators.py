"""
@author: acfromspace
"""

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(sum(a,b), difference(a,b), product(a,b), sep = '\n')