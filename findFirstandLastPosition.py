import copy
from typing import Optional, List, Tuple

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def BinarySearch(nums: List[int], st:int, end:int, target) -> int:
            if st > end:
                return st
            mid = int((st+end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return BinarySearch(nums, mid+1, end, target)
            else:
                return BinarySearch(nums, st, mid-1, target)

        index = BinarySearch(nums, 0, len(nums)-1, target)
        if index >= len(nums) or nums[index] != target:
            return [-1, -1]
        left, right = index, index
        for i in range(index, -1, -1):
            if nums[i] == target:
                left = i
            else:
                break
        for i in range(index, len(nums), 1):
            if nums[i] == target:
                right = i
            else:
                break

        return [left, right]