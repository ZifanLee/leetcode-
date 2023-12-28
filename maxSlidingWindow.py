import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [(-value, index) for index, value in enumerate(nums[:k])]
        heapq.heapify(window)
        ans = []
        for i in range(len(nums) - k + 1):
            while window[0][1] < i:
                heapq.heappop(window)
            ans.append(-window[0][0])
            if i + k < len(nums):
                heapq.heappush(window, (-nums[i+k],i+k))
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))
