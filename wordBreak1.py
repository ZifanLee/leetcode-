from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for word in wordDict:
            dic[word] = 1

        dp = [False]*len(s)

        # dp[i] 代表 s[0..i]可以由wordDic组成
        # 那么转移方程很显然，可以把 s[0...i] 划分成两部分 s[0..j], s[j+1..i]
        # 如果 s[j+1...i] in dic, dp[i] = dp[j]
        for i in range(len(s)):
            if s[:i+1] in dic:
                dp[i] = True
                continue
            for j in range(i):
                if s[j+1:i+1] in dic:
                    dp[i] = dp[j]
                    if dp[i]:
                        break

        return dp[len(s)-1]

