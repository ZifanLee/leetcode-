
# 关于字符串处理类题目心得
# 这类题目几乎一律DP，值得注意的思考点如下：
# 1. dp的长度，一般都是需要考虑空串，因此一般都是 (len(s)+1)*(len(t)+1)
# 2. 转移方程几乎一律都是考虑最后末尾字符是否匹配，从而得出
# 3. 动态规划的过程几乎一律都是1开始
# 4. 0状态需要单独初始化，根据题意思考


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if j > i:
                    break
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(s)][len(t)]

