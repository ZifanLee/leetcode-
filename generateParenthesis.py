import copy
from typing import Optional, List, Tuple

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp = ''
        ans = []
        left, right = 0, 0

        def generate():
            nonlocal tmp, ans, left, right
            if left == right == n:
                ans.append(copy.deepcopy(tmp))
                return
            if left < n:
                tmp += '('
                left += 1
                generate()
                tmp = tmp[:-1]
                left -= 1
            if right < left:
                tmp += ')'
                right += 1
                generate()
                tmp = tmp[:-1]
                right -= 1

        generate()
        return ans

solution = Solution()
print(solution.generateParenthesis(3))