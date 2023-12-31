from typing import Optional, List, Tuple

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d', 'e', 'f']
        dic['4'] = ['g', 'h', 'i']
        dic['5'] = ['j', 'k', 'l']
        dic['6'] = ['m', 'n', 'o']
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z']

        ans = []
        tmp =''

        def dfs(currentdigits: str, index: int):
            nonlocal tmp, ans
            if index == len(currentdigits):
                ans.append(tmp)
                return
            for char in dic[currentdigits[index]]:
                tmp += char
                dfs(currentdigits, index + 1)
                tmp = tmp[:-1]

        if not digits:
            return ans
        dfs(digits, 0)
        return ans



