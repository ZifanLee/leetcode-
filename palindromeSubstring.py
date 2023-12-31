import copy
from typing import Optional, List, Tuple

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []
        current = ''
        index = 0
        palindromeSet = set()

        def checkPalindrome(substring:str) -> bool:
            if substring in palindromeSet:
                return True
            st, end = 0, len(substring)-1
            while st < end:
                if substring[st] != substring[end]:
                    return False
                st += 1
                end -= 1
            palindromeSet.add(substring)
            return True

        def dfs():
            nonlocal ans, tmp, current, index
            if index == len(s):
                if not current:
                    ans.append(copy.deepcopy(tmp))
                return

            current += s[index]
            if checkPalindrome(current):
                tmp.append(copy.deepcopy(current))
                index += 1
                current = ''
                dfs()
                current = tmp[-1]
                del tmp[-1]
                index -= 1

            index += 1
            dfs()
            current = current[:-1]
            index -= 1

        dfs()
        return ans