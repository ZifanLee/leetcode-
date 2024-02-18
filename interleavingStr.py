class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(len(s1)+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
            else:
                break

        for j in range(len(s2)+1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True
            else:
                break

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1] and not dp[i][j]:
                    dp[i][j] = dp[i][j-1]

        return dp[len(s1)][len(s2)]
