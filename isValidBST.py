from typing import Optional, List
from queue import Queue
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lower(root: Optional[TreeNode]) -> int:
    if not root:
        return 999999999999
    return min(root.val, lower(root.left), lower(root.right))

def upper(root: Optional[TreeNode]) -> int:
    if not root:
        return -999999999999
    return max(root.val, upper(root.left), upper(root.right))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if upper(root.left) >= root.val or root.val >= lower(root.right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        pre = -9999999999999
        terminate = False
        def traversal(node: Optional[TreeNode]):
            nonlocal pre
            nonlocal terminate
            if not node:
                return
            traversal(node.left)
            if terminate:
                return
            if node.val <= pre:
                terminate = True
                return
            else:
                pre = node.val
            traversal(node.right)
        traversal(root)
        return not terminate



