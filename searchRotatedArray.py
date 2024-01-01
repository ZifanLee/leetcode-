import copy
from typing import Optional, List, Tuple

# 所有的二分查找的核心都是判断目标在左边还是右边
# 不要专注于寻找复杂的判断，关心在左边还是右边即可

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 虽然麻烦了点，但是还是挺快的其实
        def BinarySearch(nums: List[int], left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            mid = int((left+right)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if nums[left] <= nums[mid]:
                    return BinarySearch(nums, mid+1, right, target)
                else:
                    if nums[right] == target:
                        return right
                    elif nums[right] > target:
                        return BinarySearch(nums, mid+1, right-1, target)
                    else:
                        return BinarySearch(nums, left, mid-1, target)
            else:
                if nums[mid] <= nums[right]:
                    return BinarySearch(nums, left, mid-1, target)
                else:
                    if target == nums[left]:
                        return left
                    elif target < nums[left]:
                        return BinarySearch(nums, mid+1, right, target)
                    else:
                        return BinarySearch(nums, left+1, mid-1, target)

        # 另一个解法，核心是更加简洁的判断，但是其实并不会更快
        # 二分查找的核心永远是在左边还是在右边
        def BinarySearch_2(nums: List[int], left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return BinarySearch_2(nums, left, mid-1, target)
                else:
                    return BinarySearch(nums, mid+1, right ,target)
            else:
                if nums[mid] < target <= nums[right]:
                    return BinarySearch(nums, mid+1, right, target)
                else:
                    return BinarySearch(nums, left, mid-1, target)
        
        return BinarySearch(nums, 0, len(nums)-1, target)

solution = Solution()
print(solution.search([5,1,2,3,4], 1))