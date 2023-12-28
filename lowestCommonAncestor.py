from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []

        p_terminate, q_terminate = False, False
        def traversal(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            nonlocal p_terminate, q_terminate
            if not root:
                return
            if p_terminate and q_terminate:
                return
            if not p_terminate:
                p_path.append(root)
            if not q_terminate:
                q_path.append(root)
            if root == p:
                p_terminate = True
            if root == q:
                q_terminate = True
            traversal(root.left, p, q)
            traversal(root.right, p, q)
            if not p_terminate:
                p_path.pop(-1)
            if not q_terminate:
                q_path.pop(-1)

        traversal(root, p, q)

        index = 0
        while index < min(len(p_path), len(q_path)):
            if p_path[index] == q_path[index]:
                index += 1
            else:
                break
        return p_path[index-1]


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
solution = Solution()
solution.lowestCommonAncestor(root, root.left, root.left.right.right)
