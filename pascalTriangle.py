from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        pre = [1]
        for _ in range(numRows-1):
            current = [0]*(len(pre)+1)
            for i in range(len(current)):
                if i >=1:
                    current[i] += pre[i-1]
                if i < len(pre):
                    current[i] += pre[i]
            ans.append(current)
            pre = current
        return ans

solution = Solution()
print(solution.generate(5))
