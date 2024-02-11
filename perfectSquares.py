from typing import List
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [99 for _ in range(n)]
        for i in range(0,n):
            right = int(math.sqrt(i+1))
            if right * right == i+1:
                dp[i] = 1
                continue
            for k in range(1, right+1):
                dp[i] = min(dp[i], 1+dp[i-k*k])
        return dp[n-1]

solution = Solution()
print(solution.numSquares(192))
