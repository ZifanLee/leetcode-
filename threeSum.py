from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if num > 0:
                return ans
            if index > 0 and num == nums[index-1]:
                continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == -num:
                    ans.append([num, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif nums[i] + nums[j] > -num:
                    j -= 1
                else:
                    i += 1
        return ans
