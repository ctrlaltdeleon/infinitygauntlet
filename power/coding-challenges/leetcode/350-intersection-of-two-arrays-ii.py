"""
Notes:

Given two arrays, write a function to compute their intersection.
"""

class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        if len(nums1) < len(nums2):
            small, big = nums1, nums2
        else:
            small, big = nums2, nums1
        solution = []
        for index in big:
            print("big:", big)
            print("index:", index)
            if index in small:
                print("small:", small)
                solution.append(index)
                small.remove(index)
        return solution

test = Solution()
nums1 = [4, 9, 5]
nums2 = [5, 9, 4, 9, 8, 4]
print("intersect():", test.intersect(nums1, nums2))
nums1 = [2, 1]
nums2 = [1, 1]
print("intersect():", test.intersect(nums1, nums2))

"""
big: [5, 9, 4, 9, 8, 4]
index: 5
small: [4, 9, 5]
big: [5, 9, 4, 9, 8, 4]
index: 9
small: [4, 9]
big: [5, 9, 4, 9, 8, 4]
index: 4
small: [4]
big: [5, 9, 4, 9, 8, 4]
index: 9
big: [5, 9, 4, 9, 8, 4]
index: 8
big: [5, 9, 4, 9, 8, 4]
index: 4
intersect(): [5, 9, 4]
big: [2, 1]
index: 2
big: [2, 1]
index: 1
small: [1, 1]
intersect(): [1]
"""

"""
Time complexity: O(n). We traverse the list containing "n" elements only once.
Space complexity: O(n). To allocate the `solution` data structure.
"""