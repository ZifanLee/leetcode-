import copy
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def dfs(nums: List[float]):
            if len(nums) == 1:
                if -0.00001 < nums[0] - 24.0 < 0.00001:
                    return True
                return False
            cnt = len(nums)
            for i in range(cnt):
                for j in range(i+1, cnt):
                    op1, op2 = nums[i], nums[j]
                    tmp = [item for index, item in enumerate(nums) if index != i and index != j]
                    if dfs(tmp+[op1+op2]):
                        return True
                    if dfs(tmp+[op1-op2]):
                        return True
                    if dfs(tmp+[op2-op1]):
                        return True
                    if dfs(tmp+[op1*op2]):
                        return True
                    if op2 != 0 and dfs(tmp+[op1/op2]):
                        return True
                    if op1 != 0 and dfs(tmp+[op2/op1]):
                        return True
            return False

        return dfs([float(item) for item in cards])

solution = Solution()
print(solution.judgePoint24([3,3,8,8]))