from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node: Optional[TreeNode]):
            if not node:
                return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root