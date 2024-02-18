import copy
from typing import List

class Solution:
    def partitionSubsets(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []

        def dfs(index):
            nonlocal s
            nonlocal ans, tmp
            if index == len(s):
                ans.append(copy.copy(tmp))
                return
            if index == 0:
                tmp.append(s[index])
                dfs(index+1)
                return
            tmp.append(s[index])
            dfs(index+1)
            tmp.pop(-1)

            tmp[-1] += s[index]
            dfs(index+1)
            tmp[-1] = tmp[-1][:-1]

        dfs(0)
        return ans

solution = Solution()
print(solution.partitionSubsets("abcd"))
