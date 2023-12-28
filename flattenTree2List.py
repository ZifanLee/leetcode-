from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def convert(root: Optional[TreeNode]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
            if not root:
                return None, None
            l_st, l_end = convert(root.left)
            r_st, r_end = convert(root.right)
            if not l_st:
                root.left = None
                root.right = r_st
                end = r_end if r_end else root
                return root, end
            else:
                root.left = None
                root.right = l_st
                l_end.right = r_st
                end = r_end if r_end else l_end
                return root, end

        st, end = convert(root)
        return st

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


solution = Solution()
solution.flatten(root)
