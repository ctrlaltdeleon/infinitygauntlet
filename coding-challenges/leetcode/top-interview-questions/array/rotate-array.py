"""
@author: acfromspace
"""

"""
Notes:

Rotate a list according to the number of rotations.

I know it's not return to something, but for testing purposes I put the return statements.
"""


class Solution(object):
    def rotate1(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

    def rotate2(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = reversed(nums)
            nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])
        return nums


test = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate1():", test.rotate1(nums, k))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate2():", test.rotate2(nums, k))

"""
Time complexity : O(n).

Space complexity : O(n) for `rotate1`, O(1) for `rotate2()`.
"""
