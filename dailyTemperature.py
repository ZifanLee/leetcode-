from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_deque = deque()
        ans = [0 for _ in temperatures]
        for index, temp in enumerate(temperatures):
            if not my_deque or my_deque[-1][1] >= temp:
                my_deque.append((index,temp))
            else:
                while my_deque[-1][1] < temp:
                    i, t = my_deque.pop()
                    ans[i] = index-i
                    if not my_deque:
                        break
                my_deque.append((index, temp))

        return ans

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
