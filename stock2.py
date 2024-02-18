from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(1,len(prices)):
            profit += max(0, prices[index]-prices[index-1])
        return profit