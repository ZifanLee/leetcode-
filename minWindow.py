class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for char in t:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        st, end = 0, 0
        ismatch = len(dic)
        ans = s + "a"
        while st < len(s) and s[st] not in dic:
            st += 1
        if st == len(s):
            return ""
        dic[s[st]] -= 1
        if dic[s[st]] == 0:
            ismatch -= 1
        if ismatch == 0:
            return s[st]
        end = st + 1
        # 始终维护了[st,end)的数组，每次循环将end向后推进
        # 始终保证 s[st] 是dic中的数字，如果ismatch == 0， 那么更新ans
        # 然后将 st 推进，直到不满足条件，这个过程中可能会更新ans
        while end < len(s):
            if s[end] not in dic:
                end += 1
            else:
                dic[s[end]] -= 1
                if dic[s[end]] == 0:
                    ismatch -= 1
                end += 1
            if ismatch == 0:
                tmp = s[st:end]
                if len(tmp) < len(ans):
                    ans = tmp

                while st < end and ismatch == 0:
                    if s[st] in dic:
                        dic[s[st]] += 1
                        if dic[s[st]] == 1:
                            tmp = s[st:end]
                            if len(tmp) < len(ans):
                                ans = tmp
                            ismatch += 1
                            st += 1
                        else:
                            st += 1
                    else:
                        st += 1
                if st == end:
                    if len(ans) <= len(s):
                        return ans

        if len(ans) <= len(s):
            return ans
        else:
            return ""


s = "AA"
t = "AA"
solution = Solution()
print(solution.minWindow(s,t))