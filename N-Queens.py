import copy
from typing import Optional, List, Tuple

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        occupied = set()
        cnt = 0
        ans = []
        def format() -> List[str]:
            nonlocal occupied
            res = []
            for i in range(n):
                tmp = ''
                for j in range(n):
                    if (i, j) in occupied:
                        tmp += 'Q'
                    else:
                        tmp += '.'
                res.append(copy.deepcopy(tmp))
            return res

        def dfs():
            nonlocal columns, occupied
            nonlocal cnt, n
            if cnt == n:
                ans.append(format())
                return

            for j in range(n):
                if j not in columns:
                    valid = True
                    for pair in occupied:
                        x, y = pair
                        if y - j == x - cnt or y - j == cnt - x:
                            valid = False
                            break
                    if valid:
                        occupied.add((cnt, j))
                        columns.add(j)
                        cnt += 1
                        dfs()
                        occupied.remove((cnt-1, j))
                        columns.remove(j)
                        cnt -= 1

        dfs()
        return ans


solution = Solution()
result = solution.solveNQueens(4)
print(result)

