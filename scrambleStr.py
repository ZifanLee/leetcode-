from typing import List

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def dfs(current) -> List[str]:
            if len(current) == 1:
                return current
            res = []
            for i in range(1,len(current)):
                left, right = current[:i], current[i:]
                list1 = dfs(left)
                list2 = dfs(right)
                for l1 in list1:
                    for l2 in list2:
                        res.append(l1+l2)
                        res.append(l2+l1)
            return res

        ans = dfs(s1)
        for s in ans:
            if s == s2:
                return True
        return False

