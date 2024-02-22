from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(nums, st, end, target):
            if st > end:
                return st
            mid = (st+end)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return binary_search(nums, mid+1, end, target)
            else:
                return binary_search(nums, st, mid-1, target)

        rows = [item[0] for item in matrix]
        index = binary_search(rows,0, len(rows)-1, target)
        if index >= len(matrix):
            index -= 1

        if matrix[index][0] == target:
            return True
        elif matrix[index][0] > target:
            index -= 1
        if index < 0:
            return False
        ptr = binary_search(matrix[index], 0, len(matrix[index])-1, target)
        if ptr >= len(matrix[index]):
            return False
        if matrix[index][ptr] == target:
            return True
        else:
            return False

matrix = [[1,3,5,7]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))