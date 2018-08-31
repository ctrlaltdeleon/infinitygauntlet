"""
Created 3/12/2018

@author: acfromspace
"""

if __name__ == '__main__':
    # four integers
    a, b, c, n = (int(input()) for counter in range(4))
    
    # find combinations of lists that if the total is not != n, print
    print ([[a,b,c] for a in range(a+1) for b in range(b+1) for c in range(c+1) if (a + b + c) != n])
