import copy
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        for index, money in enumerate(nums):
            prepre = nums[index-3] if index-3>=0 else 0
            pre = nums[index-2] if index-2>=0 else 0
            nums[index] = nums[index] + max(pre,prepre)
            ans = max(ans, nums[index])
        return ans

