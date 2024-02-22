from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 5001

        def binary_search(nums, st, end):
            nonlocal ans
            if st > end:
                return
            mid = (st+end)//2
            if nums[mid] < ans:
                ans = nums[mid]
            if nums[st] <= nums[end]:
                binary_search(nums, st, mid-1)
            else:
                if nums[mid] >= nums[st]:
                    binary_search(nums, mid+1, end)
                else:
                    binary_search(nums, st, mid-1)

        binary_search(nums, 0, len(nums)-1)
        return ans


nums = [5,1,2,3,4]
solution = Solution()
print(solution.findMin(nums))