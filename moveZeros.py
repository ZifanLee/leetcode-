from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            while i < len(nums) and nums[i] == 0:
                i = i + 1
            if i == len(nums):
                while j < len(nums):
                    nums[j] = 0
                    j = j + 1
                return
            else:
                nums[j] = nums[i]
                i = i + 1
                j = j + 1


solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)