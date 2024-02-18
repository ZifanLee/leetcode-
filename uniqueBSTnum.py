from typing import List

class Solution:
    def numTrees(self, n: int) -> int:

        dic = {}

        def dfs(k) -> int:
            nonlocal dic
            if k <= 1:
                return 1
            if k in dic:
                return dic[k]
            ans = 0
            for index in range(k):
                l = dfs(index)
                if index not in dic:
                    dic[index] = l
                r = dfs(k-index-1)
                if k-index-1 not in dic:
                    dic[k-index-1] = r
                ans += l*r
            if k not in dic:
                dic[k] = ans
            return ans

        return dfs(n)