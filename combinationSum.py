import copy
from typing import Optional, List, Tuple


# 对于任何位置的元素都可以选择加进来然后继续在当前位置搜索，或者放弃当前位置，从下一个位置开始搜索
# 对于回溯问题一定要注意路径的唯一性，答案完备是一方面，路径的唯一性是无重复解的充要条件
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tmp, ans = [], []
        sum = 0
        candidates.sort()

        def dfs(index: int):
            nonlocal sum
            nonlocal tmp, ans
            if index == len(candidates) or sum + candidates[index] > target:
                return
            # 把当前值加进来
            tmp.append(candidates[index])
            sum += candidates[index]
            if sum == target:
                ans.append(copy.deepcopy(tmp))
                tmp = tmp[:-1]
                sum -= candidates[index]
                return
            # 从当前继续搜索
            dfs(index)

            # 不加当前值，直接搜索下一个
            tmp = tmp[:-1]
            sum -= candidates[index]
            dfs(index+1)

        dfs(0)
        return ans

solution = Solution()
print(solution.combinationSum([2,3,7], 7))
