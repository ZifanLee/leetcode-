from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = -math.inf
        i = 0
        ans = -math.inf
        while i < len(nums):
            preSum = max(preSum+nums[i], nums[i])
            ans= max(ans, preSum)
            i += 1
        return ans

