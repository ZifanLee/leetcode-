import copy
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        tmp = []

        def track_back(node: TreeNode, target: int):
            if not node:
                return
            if not node.left and not node.right:
                tmp.append(node.val)
                target = target - node.val
                if target == 0:
                    ans.append(copy.deepcopy(tmp))
                tmp.pop(-1)
                return

            tmp.append(node.val)
            track_back(node.left, target-node.val)
            track_back(node.right, target-node.val)
            tmp.pop(-1)

        track_back(root, targetSum)
        return ans

