"""
@author: acfromspace
"""

"""
Notes:

Alright so how do we tackle this?

J: jewels (which happen to be stones)
S: stones

Input: letters
Output: # of jewels

We need to read J and see how much of those occurrences we see in S.

Functions we'll need:

sum(iterable, start): adds the items of an iterable and returns the sum.
map(function, iterable): returns a list of the results after applying the given function to each item of a given iterable
count(): returns the number of occurrences of a substring in the given string
string1.count(string2)
    string1: main string to be checked
    string2: check occurrences of these

In this solution we use the map() for checking each element of J through count().
Compare to each element of S to see if we get a match.
For each match, we "increment" using the sum to compile all "increments".

Another possible solution checks for character in jewels matches character in stones, sum it up!

sum(if c in J for c in S)
"""


class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(J.count, S))


test_object = Solution()
J = "aA"
S = "aAABBBB"
print("Stages of the solution:")
print("Jewels: " + J)
print("Stones: " + S)
print("Number of true jewels in stones: " + str(list(map(J.count, S))))
print("Amount of jewels: " + str(test_object.numJewelsInStones(J, S)))

"""
Time complexity : O(n). Dependent on the amount of characters given in the strings.

Space complexity : O(1). Constant space is used.
"""
