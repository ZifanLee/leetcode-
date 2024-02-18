import copy
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []
        pre = ""

        def checkPalindrome(inptstr):
            i, j = 0, len(inptstr)-1
            while i < j:
                if inptstr[i] != inptstr[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(index):
            nonlocal ans, tmp
            nonlocal pre, s
            if index == len(s):
                if len(pre) > 0 and checkPalindrome(pre):
                    tmp.append(pre)
                    ans.append(copy.copy(tmp))
                    tmp.pop(-1)
                return
            if pre == "":
                pre += s[index]
                dfs(index+1)
                pre = pre[:-1]
                return

            pre += s[index]
            dfs(index+1)
            pre = pre[:-1]

            if checkPalindrome(pre):
                tmp.append(pre)
                pre = s[index]
                dfs(index+1)
                pre = tmp[-1]
                tmp.pop(-1)

        dfs(0)
        return ans



solution = Solution()
print(solution.partition("efe"))

