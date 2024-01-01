from typing import Optional, List, Tuple
from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        my_deque = deque()
        for char in s:
            if char == "]":
                tmp = ""
                pre = my_deque.pop()
                while pre != "[":
                    tmp = pre + tmp
                    pre = my_deque.pop()
                pre = my_deque.pop()
                num = ""
                while pre.isdigit():
                    num = pre + num
                    if my_deque:
                        pre = my_deque.pop()
                    else:
                        pre = "*"
                cnt = int(num)
                key = tmp * cnt
                if not pre.isdigit() and pre != "*":
                    my_deque.append(pre)
                for c in key:
                    my_deque.append(c)
            else:
                my_deque.append(char)

        return "".join(list(my_deque))

solution = Solution()
print(solution.decodeString("3[a2[bc]]3[a]"))
