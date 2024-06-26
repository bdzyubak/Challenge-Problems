# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += prices[i] - buy
                sell = prices[i]
            if prices[i] <= sell:
                buy = prices[i]
        return profit