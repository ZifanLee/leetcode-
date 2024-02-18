from typing import List


# firstbuy 代表到第 i 天为止只进行了一次买入操作
# firsetsell 代表到第 i 天为止只进行了一次买入和卖出操作
# secondbuy 代表到第 i 天为止进行了两次买入和一次卖出操作
# secondsell 代表到第 i 天为止进行了两次买入和两次卖出操作

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy = -prices[0]
        firstsell = 0
        secondbuy = -prices[0]
        secondsell = 0
        for price in prices[1:]:
            firstbuy = max(firstbuy, -price)
            firstsell = max(firstsell, firstbuy + price)
            secondbuy = max(secondbuy, firstsell - price)
            secondsell = max(secondsell, secondbuy + price)
        return secondsell