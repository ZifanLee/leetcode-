from typing import List


# 这道题的重点是 左半部分和有半部分至少有一个顺序区间
# 首先要判断左半部分是不是顺序空间
# 如果左半部分不是顺序空间，那么右半部分必定是顺序空间
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums, st, end, target):
            if st > end:
                return -1
            mid = (st+end)//2
            if nums[mid] == target:
                return mid
            elif nums[st] <= nums[mid]:
                if nums[st] <= target <= nums[mid]:
                    return binary_search(nums, st, mid-1,target)
                else:
                    return binary_search(nums, mid+1, end, target)
            elif nums[mid] <= target <= nums[end]:
                return binary_search(nums, mid+1, end, target)
            else:
                return binary_search(nums, st, mid-1, target)


        return binary_search(nums, 0, len(nums)-1, target)