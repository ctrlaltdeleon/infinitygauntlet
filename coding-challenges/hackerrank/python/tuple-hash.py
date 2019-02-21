"""
@author: acfromspace
"""

if __name__ == '__main__':
    # Take first line input, turn into int
    n = int(input())
    # Take second line input, turn into int, separated by whitespace
    integer_list = map(int, input().split())
    # Turn list into tuple
    tuple_list = tuple(integer_list)
    # Print into hash (hash is a function that takes basic data turned into complex data, think crypt passwords)
    print(hash(tuple_list))
    
    # Check if input is 0, if not, looks at next line input
    # One line function: print(input() == 0 or hash(tuple(map(int, input().split()))))