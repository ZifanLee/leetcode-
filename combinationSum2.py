import copy
from typing import List


# 全排列或者组合问题，一般都是排序之后再迭代
# 在迭代的过程中，跳过重复实现去重
# 还有重要的一点就是当前不选其实就是迭代的下一轮
# 与迭代结合的回溯一般不需要考虑当前不选的情况
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        dic = {}

        def dfs(st, target):
            nonlocal candidates
            nonlocal ans, tmp
            if target == 0:
                k = ".".join(str(e) for e in tmp)
                if k not in dic:
                    dic[k] = 1
                    ans.append(copy.copy(tmp))
                return
            if st == len(candidates) or target < 0:
                return

            tmp.append(candidates[st])
            dfs(st+1, target-candidates[st])
            tmp.pop(-1)
            dfs(st+1, target)

        candidates.sort()
        dfs(0,target)
        return ans

    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(st, target):
            nonlocal candidates
            ans = []
            if target < 0:
                return ans
            elif target == 0:
                return [[]]
            elif st == len(candidates):
                return ans
            for index in range(st, len(candidates)):
                if index > st and candidates[index] == candidates[index-1]:
                    continue
                res = dfs(index+1, target - candidates[index])
                for r in res:
                    ans.append(copy.copy([candidates[index]] + r))
            return ans

        candidates.sort()
        return dfs(0, target)

solution = Solution()
print(solution.combinationSum22([1,1,7],8))