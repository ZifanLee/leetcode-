from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lower = [0 for _ in nums]
        upper = [0 for _ in nums]
        lower[0] = nums[0]
        upper[0] = nums[0]
        ans = upper[0]
        for index in range(1, len(nums)):
            num = nums[index]
            lower[index] = min(lower[index-1]*num, upper[index-1]*num, num)
            upper[index] = max(lower[index-1]*num, upper[index-1]*num, num)
            ans = max(ans,upper[index])

        return ans

solution = Solution()
print(solution.maxProduct([2,3,-2,4]))




