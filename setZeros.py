from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in row:
            matrix[i][:] = [0]*len(matrix[0])
        for j in column:
             for i in range(len(matrix)):
                matrix[i][j] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution = Solution()
solution.setZeroes(matrix)
print(matrix)