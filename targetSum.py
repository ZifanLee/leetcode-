from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0

        def dfs(st,target):
            nonlocal nums
            nonlocal ans
            if st == len(nums):
                if target == 0:
                    ans += 1
                return
            dfs(st+1, target-nums[st])
            dfs(st+1, target+nums[st])

        dfs(0,target)
        return ans
