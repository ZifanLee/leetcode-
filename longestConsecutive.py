from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = set(nums)
        maxlength = 1
        for num in dic:
            if num-1 in dic:
                continue
            currentlen = 1
            while num+1 in dic:
                currentlen = currentlen + 1
                num = num + 1
            maxlength = max(maxlength, currentlen)
        return maxlength


