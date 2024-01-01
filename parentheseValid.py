from typing import Optional, List, Tuple
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        my_deque = deque()

        for char in s:
            if char in ["(", "[", "{"]:
                my_deque.append(char)
            else:
                if not my_deque:
                    return False
                tmp = my_deque.pop()
                if (tmp == "(" and char == ")") or (tmp == "[" and char == "]") or (tmp == "{" and char == "}"):
                    continue
                else:
                    return False

        return True if not my_deque else False

solution = Solution()
solution.isValid("()")