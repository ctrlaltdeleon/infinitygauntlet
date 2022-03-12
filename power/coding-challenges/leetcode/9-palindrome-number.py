"""
@author: acfromspace
"""

"""
Notes:

Reverse the number, did it by converting to a string.
"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


test = Solution()
true_palindrome = "12321"
false_palindrome = "123123"
print(test.is_palindrome(true_palindrome))
print(test.is_palindrome(false_palindrome))

"""
Time complexity: O(n). Go through "n" backwards once.

Space complexity: O(1). Constant space is used. 
"""
