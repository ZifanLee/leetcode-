from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = [-100]*len(nums)
        minPro = [100]*len(nums)
        maxPro[0] = nums[0]
        minPro[0] = nums[0]
        ans = maxPro[0]
        for index in range(1, len(nums)):
            maxPro[index] = max(maxPro[index-1]*nums[index], minPro[index-1]*nums[index], nums[index])
            minPro[index] = min(maxPro[index-1]*nums[index], minPro[index-1]*nums[index], nums[index])
            ans = max(ans, maxPro[index])
        return ans
