from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for index, char in enumerate(s):
            dic[char] = index

        st, end = 0, 0
        index = 0
        ans = []
        while index <= len(s)-1:
            while index <= end:
                end = max(end, dic[s[index]])
                index += 1
            ans.append(end - st + 1)
            st = index
            end = st
        return ans

solution = Solution()
print(solution.partitionLabels("eaaaabaaec"))