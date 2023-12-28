from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(l: Optional[TreeNode], r:Optional[TreeNode]) -> bool:
            if not l and not r:
                return True
            if (not l and r) or (l and not r):
                return False
            if l.val != r.val:
                return False
            if compare(l.left, r.right):
                return compare(l.right,r.left)
            else:
                return False
        if not root:
            return True
        return compare(root.left, root.right)