from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for _, str in enumerate(strs):
            key = ''.join(sorted(str))
            if key in res:
                res[key].append(str)
            else:
                res[key] = [str]
        return list(res.values())