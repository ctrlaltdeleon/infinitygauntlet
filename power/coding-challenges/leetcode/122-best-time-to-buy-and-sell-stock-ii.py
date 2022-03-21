"""
Notes:

This is more "find maximum profit" rather than finding best times to buy and sell stock.
"""

class Solution:
    def max_profit(self, prices: [int]) -> int:
        profit = 0
        for stock in range(len(prices)-1):
            if prices[stock+1] > prices[stock]:
                profit += prices[stock+1] - prices[stock]
        return profit

test = Solution()
prices = [1, 3, 5, 2, 10, 2, 1]
print("max_profit():", test.max_profit(prices))

"""
max_profit(): 12
"""

"""
Time complexity: O(n). We traverse the list containing "n" elements only once.
Space complexity: O(1). Constant space is used.
"""