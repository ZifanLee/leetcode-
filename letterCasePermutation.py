import copy
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        indexes = [index for index, item in enumerate(s) if "a"<=s[index]<="z" or "A"<=s[index]<="Z"]
        ans = []
        tmp = [char for char in s]

        def dfs(st):
            nonlocal indexes
            nonlocal ans, tmp
            if st == len(s):
                ans.append("".join(tmp))
                return
            if st not in indexes:
                dfs(st+1)
                return
            tmp[st] = tmp[st].lower()
            dfs(st+1)
            tmp[st] = tmp[st].upper()
            dfs(st+1)

        dfs(0)
        return ans
