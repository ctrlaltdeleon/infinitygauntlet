"""
Notes:

This is more "count the amount of unique elements" rather than removing duplicates.
"""

class Solution:
    def remove_duplicates(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

test = Solution()
nums = [1, 3, 5, 4, 3, 2, 9, 9, 8, 8]
print("remove_duplicates():", test.remove_duplicates(nums))

"""
remove_duplicates(): 8
"""

"""
Time complexity: O(n). We traverse the list containing "n" elements only once.
Space complexity: O(1). Constant space is used.
"""