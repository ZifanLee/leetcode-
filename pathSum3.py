from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathDic = {None: {}}
        ans = 0
        def traversal(root: Optional[TreeNode]):
            nonlocal targetSum
            nonlocal ans
            if not root:
                return
            traversal(root.left)
            traversal(root.right)
            tmp = {}
            for length, num in pathDic[root.left].items():
                if length + root.val in tmp:
                    tmp[length + root.val] += num
                else:
                    tmp[length + root.val] = num
            for length, num in pathDic[root.right].items():
                if length + root.val in tmp:
                    tmp[length + root.val] += num
                else:
                    tmp[length + root.val] = num
            if root.val in tmp:
                tmp[root.val] += 1
            else:
                tmp[root.val] = 1
            if targetSum in tmp:
                ans += tmp[targetSum]

            pathDic[root] = tmp

        traversal(root)
        return ans




