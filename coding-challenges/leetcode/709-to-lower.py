"""
@author: acfromspace
"""

"""
Notes:

Given "n" non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""


class Solution:
    def toLowerCase1(self, str: str) -> str:
        for character in str:
            if "A" <= character <= "Z":
                str = str.replace(character, chr(ord(character) + 32))
        return str

    def toLowerCase2(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

    def toLowerCase3(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

    def toLowerCase4(self, str: str) -> str:
        return str.lower()


test = Solution()
s = "HELLO there!"
print("toLowerCase1():", test.toLowerCase1(s))
print("toLowerCase2():", test.toLowerCase2(s))
print("toLowerCase3():", test.toLowerCase3(s))
print("toLowerCase4():", test.toLowerCase4(s))

"""
Time complexity : O(n). Single iteration.

Space complexity : O(1). Constant space is used. 
"""
