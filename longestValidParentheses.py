class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        ans = 0
        for index in range(1, len(s)):
            if s[index] == "(":
                continue
            if s[index-1] == "(":
                if index >= 2:
                    dp[index] = 2 + dp[index-2]
                else:
                    dp[index] = 2
                ans = max(ans, dp[index])
            elif index-1-dp[index-1] >= 0 and s[index-1-dp[index-1]] == "(":
                if index-2-dp[index-1] >= 0:
                    dp[index] = dp[index-1] + dp[index-2-dp[index-1]] + 2
                else:
                    dp[index] = dp[index - 1] + 2
                ans = max(dp[index], ans)

        return ans

solution = Solution()
solution.longestValidParentheses("(()))())(")
