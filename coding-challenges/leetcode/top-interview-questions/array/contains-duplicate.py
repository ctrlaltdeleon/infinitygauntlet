"""
@author: acfromspace
"""

"""
Notes:

Check if the list contains a duplicate or not.
"""


class Solution:
    def contains_duplicate1(self, nums: [int]) -> bool:
        nums.sort()
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                return True
        return False

    def contains_duplicate2(self, nums: [int]) -> bool:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        for i_index in range(len(nums)):
            for j_index in range(i_index + 1, len(nums)):
                if nums[j_index] == nums[i_index]:
                    return True
        return False


test = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print("contains_duplicate():", test.contains_duplicate1(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("contains_duplicate():", test.contains_duplicate1(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print("contains_duplicate():", test.contains_duplicate2(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("contains_duplicate():", test.contains_duplicate2(nums))

"""
Time complexity: O(n log n). Due to sorting time complexity will always add O(n log n).

Space complexity: O(1). This is assuming the built-in sort uses heapsort for example.
"""
