import copy
from typing import Optional, List, Tuple


# 实际上就是检测图中无环，最多2000个顶点和5000条边

class Solution:
    def canFinish(self, numCoures: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        verges = {}
        for y, x in prerequisites:
            if x in verges:
                verges[x].append(y)
            else:
                verges[x] = [y]
        path = set()
        hasCycle = False
        def dfs(st: int):
            nonlocal path, hasCycle
            nonlocal verges, visited
            if st in visited:
                return
            if st not in verges:
                visited.add(st)
                return
            for end in verges[st]:
                if end in path:
                    hasCycle = True
                    return
                path.add(end)
                dfs(end)
                if hasCycle:
                    return
                path.remove(end)
            visited.add(st)

        for x in verges.keys():
            dfs(x)
            if hasCycle:
                return False
        return True

solution = Solution()
print(solution.canFinish(2, [[1,0],[0,1]]))