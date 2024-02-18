import string

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[i] != "0":
                dp[i] += dp[i-1] if i > 0 else 1
            if i > 0 and s[i-1] != "0" and 1 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2] if i > 1 else 1

        return dp[len(s)-1]

solution = Solution()
print(solution.numDecodings("12"))