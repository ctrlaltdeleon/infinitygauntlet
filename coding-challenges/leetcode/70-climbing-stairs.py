"""
@author: acfromspace
"""

"""
Notes:

Similar to a Fibonacci solution!

Climbing to the top of the stairs takes any number of steps, but the steps taken can only be 1 step or 2 steps at a time.

How many steps does it take to reach "n"?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Edge cases.
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Formula input of f(n) = f(n-1) + f(n-2).
        step1 = 1
        step2 = 2
        for index in range(2, n):
            temp = step2
            step2 = temp + step1
            step1 = temp
        return step2


test = Solution()
test1 = 1
test2 = 8
test3 = 9
print("Number of steps needed for " + str(test1) +
      " steps:", test.climbStairs(test1))
print("Number of steps needed for " + str(test2) +
      " steps:", test.climbStairs(test2))
print("Number of steps needed for " + str(test3) +
      " steps:", test.climbStairs(test3))

"""
Time complexity : O(n). Single loop up to "n" is required to calculate "n" fibonacci number.

Space complexity : O(1). Constant space is used. 
"""
