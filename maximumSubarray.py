import copy
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        ans = nums[0]
        for index in range(1, len(nums)):
            pre = max(nums[index], nums[index]+pre)
            ans = max(ans, pre)
        return ans