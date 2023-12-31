import copy
from typing import Optional, List, Tuple

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        if not nums:
            return ans
        def dfs(currentnums: List[int]):
            nonlocal ans
            if not currentnums:
                ans.append(copy.deepcopy(tmp))
            for index in range(len(currentnums)):
                tmp.append(currentnums[index])
                currentnums.pop(index)
                dfs(currentnums)
                currentnums.insert(index,tmp[-1])
                tmp.pop(-1)

        dfs(nums)
        return ans

solution = Solution()
print(solution.permute([1,2,3]))
