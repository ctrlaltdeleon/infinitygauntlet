from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        naked = ''.join(c for c in s if c.isalpha()).lower()
        left, right = 0, len(naked) - 1

        while left < right:
            print(left, right)
            if naked[left] == naked[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

test = Solution()
input = "A man, a plan, a canal: Panama"
print("isPalindrome():", test.isPalindrome(input))