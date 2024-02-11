from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                tmp = len(word)
                if i-tmp >= 0 and s[i-tmp:i] == word:
                    if dp[i-tmp]:
                        dp[i] = True
                        continue
        return dp[len(s)]




