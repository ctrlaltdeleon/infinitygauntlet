"""
Notes:

Rotate a list according to the number of rotations.

I know it's not return to something, but for testing purposes I put the return statements.
"""

class Solution(object):
    def rotate_right1(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

    def rotate_left1(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[k:] + nums[:k]
        return nums

    def rotate_right2(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = reversed(nums)
            nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])
        return nums

    def rotate_left2(self, nums: [int], k: int) -> None:
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = reversed(nums)
            nums[:-k], nums[-k:] = reversed(nums[:-k]), reversed(nums[-k:])
        return nums

test = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate_right1():", test.rotate_right1(nums, k))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate_left1():", test.rotate_left1(nums, k))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate_right2():", test.rotate_right2(nums, k))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("rotate_left2():", test.rotate_left2(nums, k))

"""
rotate_right1(): [7, 8, 9, 1, 2, 3, 4, 5, 6]
rotate_left1(): [4, 5, 6, 7, 8, 9, 1, 2, 3]
rotate_right2(): [7, 8, 9, 1, 2, 3, 4, 5, 6]
rotate_left2(): [4, 5, 6, 7, 8, 9, 1, 2, 3]
"""

"""
Time complexity: O(n).
Space complexity: O(n).
"""