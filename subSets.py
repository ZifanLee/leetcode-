import copy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def track_back(i: int):
            nonlocal nums
            if i == len(nums):
                ans.append(copy.deepcopy(tmp))
                return
            track_back(i+1)

            tmp.append(nums[i])
            track_back(i+1)
            tmp.pop(-1)

        track_back(0)
        return ans

solution = Solution()
print(solution.subsets([1,2,3]))