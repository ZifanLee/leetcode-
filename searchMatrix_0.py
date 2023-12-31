import copy
from typing import Optional, List, Tuple

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def BinarySearch(nums:List[int], st:int, end:int, target) -> int:
            if st > end:
                return end
            mid = int((st+end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return BinarySearch(nums, mid+1, end, target)
            else:
                return BinarySearch(nums, st, mid-1, target)

        coloumn = [row[0] for row in matrix]
        index = BinarySearch(coloumn, 0, len(coloumn)-1, target)
        if index < 0:
            return False
        if target == coloumn[index]:
            return True
        row_index = BinarySearch(matrix[index], 0, len(matrix[index])-1, target)
        if matrix[index][row_index] == target:
            return True
        return False

solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(solution.searchMatrix(matrix, 3))
