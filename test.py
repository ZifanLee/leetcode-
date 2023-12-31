from typing import Optional, List, Tuple

nums = [1,3,5,6]
digits = ''
i, j = 1, 10
fresh = set()

# 这个是一个很重要的基本的算法，二分查找
def BinarySearch(nums: List[int], st: int, end: int, target) -> int:
    if st > end:
        return st
    mid = int((st + end) / 2)
    if nums[mid] == target:
        return end
    elif nums[mid] < target:
        return BinarySearch(nums, mid + 1, end, target)
    else:
        return BinarySearch(nums, st, mid - 1, target)

print(BinarySearch(nums, 0 ,3, -1))