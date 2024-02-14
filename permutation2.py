import copy
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        dic = {}

        def dfs(remain):
            nonlocal ans, tmp
            if len(remain) == 0:
                nums_str = ".".join([str(e) for e in tmp])
                if nums_str in dic:
                    return
                dic[nums_str] = 1
                ans.append(copy.copy(tmp))
            for index in range(0, len(remain)):
                tmp.append(remain[index])
                dfs(remain[:index] + remain[index+1:])
                tmp.pop(-1)

        dfs(nums)
        return ans


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def track_back(remain):
            ans = []
            if len(remain) == 1:
                return [remain]
            for index in range(len(remain)):
                if index > 0 and remain[index] == remain[index-1]:
                    continue
                res = track_back(remain[:index]+remain[index+1:])
                for r in res:
                    ans.append([remain[index]]+r)
            return ans

        nums.sort()
        return track_back(nums)

solution = Solution2()
print(solution.permuteUnique([1,2,3]))