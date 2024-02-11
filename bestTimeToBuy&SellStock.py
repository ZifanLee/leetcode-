from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxp = 0
        currentp = 0
        pre = prices[0]
        for p in prices:
            currentp = max(0, currentp + p - pre)
            pre = p
            maxp = max(maxp, currentp)
        return maxp

        