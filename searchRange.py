from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = len(nums), -1

        def search_left(nums, st, end, target):
            if st > end:
                return
            nonlocal left
            mid = (st+end)//2
            if nums[mid] == target:
                left = min(left, mid)
                search_left(nums, st, mid-1, target)
            elif nums[mid] < target:
                search_left(nums, mid+1, end, target)
            else:
                search_left(nums, st, mid-1, target)

        def search_right(nums, st, end, target):
            if st > end:
                return
            nonlocal right
            mid = (st+end)//2
            if nums[mid] == target:
                right = max(right, mid)
                search_right(nums, mid+1, end, target)
            elif nums[mid] < target:
                search_right(nums, mid+1, end, target)
            else:
                search_right(nums, st, mid-1, target)

        search_left(nums, 0, len(nums)-1, target)
        if left == len(nums):
            return [-1, -1]
        else:
            search_right(nums, 0, len(nums)-1, target)
            return [left, right]

nums = [5,7,7,8,8,10]
solution = Solution()
print(solution.searchRange(nums, 8))