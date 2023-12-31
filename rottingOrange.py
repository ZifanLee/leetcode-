import copy
from typing import Optional, List, Tuple


# 有两个思路： 由于gird最多是10*10， 那么最多10次迭代之后，就没有 new rotten oranges
# 第二个思路就是对每一个 rotten orange 引入一个新的状态，rotten ending,意为不再能够感染附近orange，可以从rotten中去掉
# 思路二显然更加迅速

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.append((i, j))

        if not fresh:
            return 0

        def rot(i: int, j: int):
            nonlocal fresh, rotten
            nonlocal grid
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == 1:
                fresh.remove((i, j))
                grid[i][j] = 2
                rotten.append((i, j))

        def bfs():
            nonlocal rotten, fresh, grid
            tmplength = len(rotten)
            for i in range(tmplength):
                x, y = rotten[i]
                rot(x + 1, y)
                rot(x - 1, y)
                rot(x, y + 1)
                rot(x, y - 1)
            rotten = rotten[tmplength:]

        ans = 0
        while rotten:
            ans += 1
            bfs()

        return ans-1 if len(fresh) == 0 else -1

solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))