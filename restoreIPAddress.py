from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        tmp = []
        length = 0

        def valid(str):
            if str[0] == "0" and len(str) > 1:
                return False
            else:
                return True

        def track_back(st):
            nonlocal s
            nonlocal tmp
            nonlocal length
            if length > 4:
                return
            if length == 4:
                if st == len(s):
                    ans.append(".".join(tmp))
                return
            for i in range(1,4):
                if st + i > len(s):
                    break
                current = s[st:st+i]
                if valid(current) and 0 <= int(current) <= 255:
                    length += 1
                    tmp.append(current)
                    track_back(st+i)
                    tmp.pop(-1)
                    length -= 1

        track_back(0)
        return ans

solution = Solution()
print(solution.restoreIpAddresses("25525511135"))

