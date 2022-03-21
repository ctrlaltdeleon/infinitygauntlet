"""
Write a function: 

def missing_integer(A):
    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def missing_integer(A):
    for index in range(1, len(A)):
        if index not in A:
            return index
    return len(A)+1

example1 = [1, 3, 6, 4, 1, 2]
example2 = [1, 2, 3]
example3 = [-1, -3]
print(missing_integer(example1))
print(missing_integer(example2))
print(missing_integer(example3))

"""
5
4
1
"""