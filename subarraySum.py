from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        total = 0
        ans = 0
        dic[0] = 1
        for index, num in enumerate(nums):
            total += num
            if total-k in dic:
                ans += dic[total-k]
            if total in dic:
                dic[total] += 1
            else:
                dic[total] = 1
        return ans

nums = [1,1,1]
k = 0
solution = Solution()
print(solution.subarraySum(nums, k))