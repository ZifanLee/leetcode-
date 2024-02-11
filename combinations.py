import copy
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        ans = []
        tmp = []

        def dfs(st):
            nonlocal k
            nonlocal nums, ans, tmp
            if len(tmp) == k:
                ans.append(copy.copy(tmp))
                return
            for index in range(st, len(nums)):
                tmp.append(nums[index])
                dfs(index+1)
                tmp.pop(-1)

        dfs(0)
        return ans

solution = Solution()
print(solution.combine(4,2))