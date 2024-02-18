import copy


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        tmp = [False]*len(s)
        dp = []
        for _ in range(len(s)):
            dp.append(copy.copy(tmp))
        for index in range(len(s)):
            dp[index][index] = True

        for length in range(2, len(s)+1):
            for st in range(len(s)):
                if st+length > len(s):
                    break
                end = st+length-1
                if length == 2:
                    if s[st] == s[end]:
                        dp[st][end] = True
                        if len(ans) < length:
                            ans = s[st:end+1]
                    continue
                if s[st] == s[end] and dp[st+1][end-1]:
                    dp[st][end] = True
                    if len(ans) < length:
                        ans = s[st:end+1]

        return ans


solution = Solution()
print(solution.longestPalindrome("bb"))