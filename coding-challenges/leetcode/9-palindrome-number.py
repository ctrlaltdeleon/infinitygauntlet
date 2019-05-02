"""
@author: acfromspace
"""

"""
Notes:

Reverse the number, did it by converting to a string.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


"""
Time complexity : O(n). Go through "n" backwards once.

Space complexity : O(1). Constant space is used. 
"""
