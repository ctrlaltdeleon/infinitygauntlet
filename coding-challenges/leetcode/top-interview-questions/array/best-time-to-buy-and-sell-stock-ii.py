"""
@author: acfromspace
"""

"""
Notes:

This is more "find maximum profit" rather than finding best times to buy and sell stock.
"""


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        for stock in range(len(prices)-1):
            if prices[stock+1] > prices[stock]:
                profit += prices[stock+1] - prices[stock]
        return profit


"""
Time complexity : O(n). We traverse the list containing "n" elements only once.

Space complexity : O(1). Constant space is used.
"""
