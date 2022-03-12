"""
@author: acfromspace
"""


class Solution:
    def range(self, list1):
        highest = list1[0]
        lowest = list1[0]
        highest2 = None
        lowest2 = None
        lowest3 = None
        for index in list1:
            if index > highest:
                highest2 = highest
                highest = index
            elif highest2 == None or index > highest2:
                highest2 = index
            if index < lowest:
                lowest3 = lowest2
                lowest2 = lowest
                lowest = index
            elif lowest2 == None or index < lowest2:
                lowest3 = lowest2
                lowest2 = index
            elif lowest3 == None or index < lowest3:
                lowest3 = index
        print("Lowest:", lowest)
        print("2nd lowest:", lowest2)
        print("3rd lowest:", lowest3)
        print("Highest:", highest)
        print("2nd highest:", highest2)


list1 = [5, 3, 2, 0, 0, 6, 3]
s = Solution()
s.range(list1)
