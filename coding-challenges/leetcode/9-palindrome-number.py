"""
@author: acfromspace
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        data = str(x)
        return True if data == data[::-1] else False
