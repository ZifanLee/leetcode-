import copy
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def construct(st: int, end: int) -> List[Optional[TreeNode]]:
            ans = []
            if st > end:
                ans.append(None)
                return ans
            for i in range(st, end + 1):
                root = TreeNode(val=i)
                lefts = construct(st, i - 1)
                rights = construct(i + 1, end)
                for l in lefts:
                    for r in rights:
                        root.left = l
                        root.right = r
                        ans.append(copy.copy(root))
            return ans

        return construct(1, n)


solution = Solution()
solution.generateTrees(2)