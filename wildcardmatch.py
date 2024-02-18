import copy


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tmp = [False]*(len(p)+1)
        dp = []
        for _ in range(len(s)+1):
            dp.append(copy.copy(tmp))
        dp[0][0] = True

        # dp[i][j] 代表s前i个前缀能否匹配p前i个前缀

        if len(p) > 0:
            index = 0
            while index < len(p) and p[index] == "*":
                dp[0][index+1] = True
                index += 1

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j].isalpha():
                    if s[i] != p[j]:
                        continue
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "?":
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        return dp[len(s)][len(p)]

solution = Solution()
print(solution.isMatch(s = "adceb", p = "*a*b"))