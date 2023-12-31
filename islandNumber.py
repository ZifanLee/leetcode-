import copy
from typing import Optional, List, Tuple

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        occupied = [[False for _ in row] for row in grid]
        cnt = 0
        def dfs(i: int, j:int):
            if i < 0 or i >= len(occupied) or j < 0 or j >= len(occupied[0]):
                return
            if occupied[i][j] or grid[i][j] == "0":
                return
            occupied[i][j] = True
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not occupied[i][j] and grid[i][j] == "1":
                    cnt += 1
                    dfs(i,j)

        return cnt
