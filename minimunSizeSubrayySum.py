from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = nums[0]
        ans = len(nums)+1
        while r < len(nums):
            while r < len(nums) and total < target:
                r += 1
                if r == len(nums):
                    break
                total += nums[r]

            while l <= r and total >= target:
                ans = min(ans, r-l+1)
                total -= nums[l]
                l += 1

        if ans == len(nums)+1:
            return 0
        else:
            return ans

target = 1
nums = [2,3,1,2,4,3]
solution = Solution()
print(solution.minSubArrayLen(target, nums))
