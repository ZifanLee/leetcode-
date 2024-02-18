import copy
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        tmp = []

        def dfs(st):
            nonlocal graph
            if st == len(graph)-1:
                tmp.append(st)
                ans.append(copy.copy(tmp))
                tmp.pop(-1)
                return
            tmp.append(st)
            for next_des in graph[st]:
                dfs(next_des)
            tmp.pop(-1)

        dfs(0)
        return ans
