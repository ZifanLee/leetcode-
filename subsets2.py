import copy
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        dic = {}

        def tract_back(i):
            nonlocal nums, ans
            if i == len(nums):
                tmpstr = ".".join([str(e) for e in tmp])
                if tmpstr in dic:
                    return
                dic[tmpstr] = 0
                ans.append(copy.copy(tmp))
                return
            tmp.append(nums[i])
            tract_back(i+1)
            tmp.pop(-1)
            tract_back(i+1)


        nums.sort()
        tract_back(0)
        return ans

solution = Solution()
print(solution.subsetsWithDup([1,2,2]))
