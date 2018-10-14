# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0

# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

"""
Alright so how do we tackle this?

J: jewels (which happen to be stones)
S: stones

Input: letters
Output: # of jewels

We need to read J and see how much of those occurrences we see in S.

Functions we'll need:

sum(): adds the items of an iterable and returns the sum
sum(iter, start):
    iter: iterable to be summed
    start (optional): another value to be added to the iterable

map(): returns a list of the results after applying the given function to each item of a given iterable
map(fun, iter):
    fun: function to which map passes each element to iterable
    iterable: iterable to be mapped
    
.count: returns the number of occurrences of a substring in the given string

In this problem
"""

# class Solution:
#     def numJewelsInStones(self, J, S):
#         return sum(map(J.count, S))

if __name__ == '__main__':

J = "aA"
S = "aAABBBB"

print(J, S)
