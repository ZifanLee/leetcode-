from typing import Optional, List, Tuple

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def BinarySearch(nums: List[int], left: int, right: int) -> int:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                return BinarySearch(nums, min(mid+1, right), right)
            else:
                return BinarySearch(nums, left+1, max(mid, left+1))

        return BinarySearch(nums, 0, len(nums)-1)


solution = Solution()
print(solution.findMin([3,4,5,1,2]))

