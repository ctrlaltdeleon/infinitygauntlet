"""
@author: acfromspace
"""

"""
Notes:

Rotate a list according to the number of rotations.
"""


class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_optimized(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % len(nums)
        j = 0
        while n > 0 and k % n != 0:
            for i in range(k):
                nums[j + i], nums[len(nums) - k +
                                  i] = nums[len(nums) - k + i], nums[j + i]
            n = n - k
            j = j + k
            k = k % n


"""
Time complexity : O(n).

Space complexity : O(n) for `rotate`, O(1) for `rotate_optimized()`.
"""
