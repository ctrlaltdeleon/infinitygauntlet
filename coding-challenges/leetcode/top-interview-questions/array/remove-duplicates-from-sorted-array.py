"""
@author: acfromspace
"""

"""
Notes:

This is more "count the amount of unique elements" rather than removing duplicates.
"""


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


"""
Time complexity : O(n). We traverse the list containing "n" elements only once.

Space complexity : O(1). Constant space is used.
"""
