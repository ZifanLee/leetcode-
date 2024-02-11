from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre, prepre = 2,1
        current = 0
        for _ in range(2,n):
            current = prepre + pre
            prepre = pre
            pre = current
        return current


solution = Solution()
print(solution.climbStairs(4))