import copy
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        k = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                k[i][j] = k[i][j-1] + 1 if j > 0 else 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if k[i][j] == 0:
                    continue
                left = k[i][j]
                ans = max(ans, k[i][j])
                for index in range(i-1,-1,-1):
                    left = min(left, k[index][j])
                    if left == 0:
                        break
                    ans = max(ans, left*(i-index+1))

        return ans
