"""
Notes:

Given "n" non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

class Solution:
    def to_lower_case1(self, str: str) -> str:
        for character in str:
            if "A" <= character <= "Z":
                str = str.replace(character, chr(ord(character) + 32))
        return str

    def to_lower_case2(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

    def to_lower_case3(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

    def to_lower_case4(self, str: str) -> str:
        return str.lower()

test = Solution()
s = "HELLO there!"
print("to_lower_case1():", test.to_lower_case1(s))
print("to_lower_case2():", test.to_lower_case2(s))
print("to_lower_case3():", test.to_lower_case3(s))
print("to_lower_case4():", test.to_lower_case4(s))

"""
to_lower_case1(): hello there!
to_lower_case2(): hello there!
to_lower_case3(): hello there!
to_lower_case4(): hello there!
"""

"""
Time complexity: O(n). Single iteration.
Space complexity: O(1). Constant space is used. 
"""