from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dic = {}
        ans = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal dic
            nonlocal ans
            if not node:
                return 0
            if node in dic:
                return dic[node]
            l = dfs(node.left)
            r = dfs(node.right)
            dic[node] = max(node.val, node.val +l, node.val+r)
            ans = max(ans, node.val, node.val+l, node.val+r, node.val+l+r)
            return dic[node]

        dfs(root)
        return ans