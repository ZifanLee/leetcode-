from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = 0
        terminate = False
        def traversal(node: Optional[TreeNode]):
            nonlocal cnt
            nonlocal ans
            nonlocal terminate
            if not node:
                return
            traversal(node.left)
            if terminate:
                return
            cnt += 1
            if cnt == k:
                ans = node.val
                terminate = True
                return
            traversal(node.right)

        traversal(root)
        return ans