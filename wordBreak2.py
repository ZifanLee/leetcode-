import copy
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = {}
        for word in wordDict:
            dic[word] = 1

        ans = []
        tmp = []
        pre = ""

        def dfs(index):
            nonlocal pre
            nonlocal ans, tmp
            if index == len(s):
                if pre in dic:
                    tmp.append(pre)
                    ans.append(" ".join(tmp))
                    tmp.pop(-1)
                    return
                elif pre == "":
                    ans.append(" ".join(tmp))
                    return
                return
            pre += s[index]
            dfs(index+1)
            pre = pre[:-1]

            if pre in dic:
                tmp.append(pre)
                pre = s[index]
                dfs(index+1)
                pre = tmp[-1]
                tmp.pop(-1)

        dfs(0)
        return ans

