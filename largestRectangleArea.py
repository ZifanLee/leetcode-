from collections import deque
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0 for _ in heights]
        right = [0 for _ in heights]
        stack = deque()
        for index, h in enumerate(heights):
            if not stack:
                stack.append((index, h))
            elif h >= stack[-1][1]:
                stack.append((index, h))
            else:
                while stack[-1][1] > h:
                    right[stack[-1][0]] = index
                    stack.pop()
                    if not stack:
                        break
                stack.append((index, h))
        while stack:
            index, _ = stack.pop()
            right[index] = len(heights)
        stack.clear()

        for index in range(len(heights)-1, -1, -1):
            h = heights[index]
            if not stack:
                stack.append((index, h))
            elif h >= stack[-1][1]:
                stack.append((index, h))
            else:
                while stack[-1][1] > h:
                    left[stack[-1][0]] = index
                    stack.pop()
                    if not stack:
                        break
                stack.append((index, h))
        while stack:
            index, _ = stack.pop()
            left[index] = -1

        ans = 0
        for index in range(len(heights)):
            ans = max((right[index]-left[index]-1)*heights[index], ans)
        return ans


solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))
