from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for index, num in enumerate(nums):
            if index > reach:
                return False
            reach = max(index + num, reach)
            if reach >= len(nums) - 1:
                return True
        return True
