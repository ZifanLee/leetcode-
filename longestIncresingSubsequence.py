from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        ans =1
        for i in range(0, len(nums)):
            for index, num in enumerate(nums):
                if index >= i:
                    break
                if num < nums[i]:
                    dp[i] = max(dp[i], dp[index]+1)
            ans = max(ans, dp[i])
        return ans