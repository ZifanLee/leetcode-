import copy
from typing import Optional, List, Tuple

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        tmp = []
        def dfs(nums: List[int], index: int):
            if 0 < index < len(nums) and nums[index] == nums[index - 1]:
                return
            if index == len(nums):
                ans.append(copy.deepcopy(tmp))
                return
            tmp.append(nums[index])
            dfs(nums, index+1)
            tmp.pop(-1)
            dfs(nums, index+1)

        dfs(nums, 0)
        return ans


