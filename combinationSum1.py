import copy
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []

        def dfs(st, target):
            nonlocal candidates
            if target == 0:
                ans.append(copy.copy(tmp))
                return
            elif target < 0:
                return
            elif st >= len(candidates):
                return
            tmp.append(candidates[st])
            dfs(st, target-candidates[st])
            tmp.pop(-1)
            dfs(st+1, target)

        candidates.sort()
        dfs(0, target)
        return ans