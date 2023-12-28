from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        zeroCnt = 0
        ptr = 0
        for index, num in enumerate(nums):
            if num == 0:
                zeroCnt += 1
                ptr = index
                if zeroCnt > 1:
                    return [0]*len(nums)
                continue
            product *= num
        if zeroCnt != 0:
            ans = [0]*len(nums)
            ans[ptr] = product
            return ans
        ans = [0] * len(nums)
        for index, num in enumerate(nums):
            ans[index] = int(product / num)
        return ans
