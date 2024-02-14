import copy
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        dic = {}

        def dfs(st):
            nonlocal nums
            nonlocal ans, tmp, dic
            if st == len(nums):
                if len(tmp) > 1:
                    tmp_str = ".".join(str(e) for e in tmp)
                    if tmp_str not in dic:
                        dic[tmp_str] = 1
                        ans.append(copy.copy(tmp))
                return
            if len(tmp) == 0:
                tmp.append(nums[st])
                dfs(st+1)
                tmp.pop(-1)
                dfs(st+1)
                return
            if nums[st] >= tmp[-1]:
                tmp.append(nums[st])
                dfs(st + 1)
                tmp.pop(-1)
            dfs(st + 1)

        dfs(0)
        return ans


solution = Solution()
print(solution.findSubsequences2([4,6,7,7]))


