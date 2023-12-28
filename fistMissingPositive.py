from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = 1
        ans = 1
        while True:
            if ans not in dic:
                return ans
            ans += 1
