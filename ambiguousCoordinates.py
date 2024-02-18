from typing import List
import re

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        tmp = []
        for item in s[1:-1]:
            tmp.append(item)
            tmp.append("")
        tmp.pop(-1)

        def checkValid() -> bool:
            tmp_op = "".join(tmp).split(",")
            if len(tmp_op) != 2:
                return False
            op1, op2 = tmp_op[0],tmp_op[1]
            patterns = r"^(0|[1-9][0-9]*)(\.[0-9]*[1-9])?$"
            if re.fullmatch(patterns,op1) and re.fullmatch(patterns, op2):
                return True
            else:
                return False


        def dfs(index:int, hascomma: bool, pointnum:int):
            if (hascomma and pointnum == 2) or (index >= len(tmp)):
                if checkValid():
                    tmp_op = "".join(tmp).split(",")
                    ans.append("(" + ", ".join(tmp_op) + ")")
                return
            if not hascomma:
                tmp[index] = ","
                dfs(index+2, True, pointnum)
                tmp[index] = ""
            if pointnum < 2:
                tmp[index] = "."
                dfs(index+2, hascomma, pointnum+1)
                tmp[index] = ""
            dfs(index+2, hascomma, pointnum)

        dfs(1, False, 0)
        return ans


solution = Solution()
print(solution.ambiguousCoordinates("(123)"))

