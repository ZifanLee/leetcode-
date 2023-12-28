from typing import List
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        duplicate = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[j][-(i+1)] = duplicate[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)
print(matrix)