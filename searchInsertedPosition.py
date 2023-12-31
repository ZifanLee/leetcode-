import copy
from typing import Optional, List, Tuple

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def BinarySearch(st: int, end:int, target:int) -> int:
            nonlocal nums
            if st > end:
                return st
            med = int((st+end)/2)
            if nums[med] == target:
                return med
            elif nums[med] < target:
                return BinarySearch(med+1, end, target)
            else:
                return BinarySearch(st, med, target)

        return BinarySearch(0, len(nums)-1, target)