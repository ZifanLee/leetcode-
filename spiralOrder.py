from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        ptr = [0, 0]
        total = len(matrix) * len(matrix[0])
        while matrix:
            while matrix and ptr[1] < len(matrix[0]):
                ans.append(matrix[ptr[0]][ptr[1]])
                ptr[1] += 1
            ptr[1] -= 1
            if matrix:
                del matrix[ptr[0]]
            else:
                return ans
            if len(ans) == total:
                return ans

            while matrix and ptr[0] < len(matrix):
                ans.append(matrix[ptr[0]][ptr[1]])
                del matrix[ptr[0]][ptr[1]]
                ptr[0] += 1
            ptr[0] -= 1
            ptr[1] -= 1
            if len(ans) == total:
                return ans

            while matrix and ptr[1] >= 0:
                ans.append(matrix[ptr[0]][ptr[1]])
                ptr[1] -= 1
            ptr[1] = 0
            if matrix:
                del matrix[ptr[0]]
            else:
                return ans
            if len(ans) == total:
                return ans
            ptr[0] -= 1

            while matrix and ptr[0] >= 0:
                ans.append(matrix[ptr[0]][ptr[1]])
                del matrix[ptr[0]][ptr[1]]
                ptr[0] -= 1
            if len(ans) == total:
                return ans
            ptr[0] = 0
        return ans

matrix = [[1],[2],[3]]
solution = Solution()
print(solution.spiralOrder(matrix))

