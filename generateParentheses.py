from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        tmp = ""

        def dfs(left, right):
            nonlocal tmp, ans
            nonlocal n
            if left == 0 and right == 0:
                ans.append(tmp)
            if 0 < left:
                tmp += "("
                dfs(left-1, right)
                tmp = tmp[:-1]
            if right > left:
                tmp += ")"
                dfs(left, right-1)
                tmp = tmp[:-1]

        dfs(n, n)
        return ans

solution = Solution()
print(solution.generateParenthesis(3))