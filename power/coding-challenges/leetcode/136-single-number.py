class Solution:
    def single_number1(self, nums: [int]) -> int:
        # Time: O(n^2).
        # Space: O(n).
        seen = []
        for index in nums:
            if index not in seen:
                seen.append(index)
            else:
                seen.remove(index)
        return seen.pop()

    def single_number2(self, nums: [int]) -> int:
        # Time: O(n).
        # Space: O(n).
        hash_table = {}
        for index in nums:
            try:
                hash_table.pop(index)
            except:
                hash_table[index] = 1
        return hash_table.popitem()[0]

    def single_number3(self, nums: [int]) -> int:
        # Time: O(n).
        # Space: O(n).
        return 2 * sum(set(nums)) - sum(nums)

    def single_number4(self, nums: [int]) -> int:
        # Time: O(n).
        # Space: O(1).
        bit = 0
        for index in nums:
            bit ^= index
        return bit

test = Solution()
nums = [4, 1, 2, 1, 2]
print("single_number1():", test.single_number1(nums))
print("single_number2():", test.single_number2(nums))
print("single_number3():", test.single_number3(nums))
print("single_number4():", test.single_number4(nums))

"""
single_number1(): 4
single_number2(): 4
single_number3(): 4
single_number4(): 4
"""