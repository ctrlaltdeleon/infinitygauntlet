"""
@author: acfromspace
"""

"""
Notes:

Reverse the number, did it by converting to a string.
"""


class Solution:
    def trap(self, height):
        total_water, left_max, right_max, low, high = 0, 0, 0, 0, len(height)-1

        while(low < high):
            if(height[low] < height[high]):
                if(height[low] > left_max):
                    left_max = height[low]
                else:
                    total_water += left_max - height[low]
                low += 1
            else:
                if(height[high] > right_max):
                    right_max = height[high]
                else:
                    total_water += right_max - height[high]
                high -= 1

        return total_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution.trap(height))

"""
Time complexity : O(n). Single iteration.

Space complexity : O(1). Constant space is used. 
"""
