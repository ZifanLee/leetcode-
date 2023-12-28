from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = root.val
        pathDic = {None:0}

        def traversal(root: Optional[TreeNode]):
            nonlocal ans, pathDic
            if not root:
                return
            traversal(root.left)
            traversal(root.right)
            pathDic[root] = max(root.val, root.val + pathDic[root.left], root.val + pathDic[root.right])
            tmp = max(pathDic[root], root.val + pathDic[root.left] + pathDic[root.right])
            ans = max(ans, tmp)

        traversal(root)
        return ans
