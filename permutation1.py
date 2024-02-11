import copy
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []

        def dfs(dfs_nums):
            if len(dfs_nums) == 0:
                ans.append(copy.copy(tmp))
                return
            for index in range(0, len(dfs_nums)):
                tmp.append(dfs_nums[index])
                dfs(dfs_nums[0:index]+dfs_nums[index+1:])
                tmp.pop(-1)

        dfs(nums)
        return ans

solution = Solution()
print(solution.permute([1,2,3]))