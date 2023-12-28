from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node: Optional[TreeNode]):
            if not node:
                return
            traversal(node.left)
            ans.append(node.val)
            traversal(node.right)

        traversal(root)
        return ans