from typing import List


# 这种逻辑太无聊了，不如直接线性查找了
# 下面是针对无重复数字的情况，会这个就行了
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(nums, st, end, target):
            if st > end:
                return False
            mid = (st + end) // 2
            if nums[mid] == target:
                return True
            elif nums[st] <= nums[mid]:
                if nums[st] <= target <= nums[mid]:
                    return binary_search(nums, st, mid - 1, target)
                else:
                    return binary_search(nums, mid+1, end, target)
            else:
                if nums[mid] <= target <= nums[end]:
                    return binary_search(nums, mid+1, end, target)
                else:
                    return binary_search(nums, st, mid-1, target)

        return binary_search(nums, 0, len(nums)-1, target)

nums = [1,0,1,1,1]
target = 0
solution = Solution()
print(solution.search(nums, target))