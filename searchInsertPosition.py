from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binary_search(nums, st, end, target):
            if st > end:
                return st
            mid = (st+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, mid+1, end, target)
            else:
                return binary_search(nums, st, mid-1, target)

        return binary_search(nums, 0, len(nums)-1, target)

nums = [1,3,5,6]
solution = Solution()
print(solution.searchInsert(nums, -1))