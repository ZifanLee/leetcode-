from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for index, ele in enumerate(nums):
            if target - ele in dic:
                return [dic[target - ele], index]
            else:
                dic[ele] = index

# Example usage:
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)