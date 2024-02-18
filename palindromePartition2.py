class Solution:
    def minCut(self, s: str) -> int:
        isPan = [[False] * len(s) for _ in range(len(s))]

        # 外层循环len代表长度，即 r-l 的差值，实际上是从0开始
        # 内存循环代表起始位置
        # 规划出s[i--j]是否是 palindrome
        for length in range(len(s)):
            for i in range(len(s)):
                if i + length >= len(s):
                    break
                if length == 0:
                    isPan[i][i + length] = True
                    continue
                if length == 1:
                    isPan[i][i + length] = s[i] == s[i + length]
                    continue
                isPan[i][i + length] = s[i] == s[i + length] and isPan[i + 1][i + length - 1]

        # dp[i] 代表s[0...i]划分成回文串序列最少需要划分多少次
        # 很显然如果 isPan[0][i], 那么dp[i] = 0
        # 否则可以把 s[0..i]划分成两部分, s[0..j] s[j+1....i]
        # 如果 s[j+1....i] 是回文串，那么 dp[i] = dp[j] + 1
        dp = [len(s) - 1] * len(s)

        for i in range(len(s)):
            if isPan[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if isPan[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[len(s) - 1]
