from typing import List

class Solution:
    # 贪心版本
    def jump(self, nums: List[int]) -> int:
        begin, end = 0, 0
        cnt = 0
        while end < len(nums)-1:
            cnt += 1
            tmp = end
            for i in range(begin, end+1):
                tmp = max(tmp, i + nums[i])
            begin = end+1
            end = tmp
        return cnt

    # 动态规划版
    def jump2(self, nums: List[int]) -> int:
        cnt = [999999 for _ in nums]
        cnt[0] = 0
        for index, num in enumerate(nums):
            for i in range(1, num+1):
                if index + i >= len(nums):
                    break
                cnt[index+i] = min(cnt[index+i], cnt[index]+1)
        return cnt[len(nums)-1]
