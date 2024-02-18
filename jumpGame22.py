from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        st, end = 0,0
        ans = 0
        while end < len(nums)-1:
            origin = end
            for index in range(st,end+1):
                end = max(end, index + nums[index])
            st = origin + 1
            ans += 1
        return ans
