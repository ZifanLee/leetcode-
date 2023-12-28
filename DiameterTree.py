from typing import Optional, List
from queue import Queue
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(nums: Optional[List[int]]) -> Optional[TreeNode]:
    index = 0
    if not nums:
        return None
    root = TreeNode(nums[index])
    q = Queue(maxsize=0)
    q.put(root)
    index += 1
    while index < len(nums):
        cnt = q.qsize()
        while cnt >= 0:
            if index >= len(nums):
                break
            node = q.get()
            cnt -= 1
            if nums[index] != math.inf:
                l = TreeNode(nums[index])
                node.left = l
                index += 1
                q.put(l)
            else:
                index += 1
            if index >= len(nums):
                break
            if nums[index] != math.inf:
                r = TreeNode(nums[index])
                node.right = r
                index += 1
                q.put(r)
            else:
                index += 1
    return root

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = {None: 0}

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal dic
            if node in dic:
                return dic[node]
            l = depth(node.left)
            r = depth(node.right)
            if node.left not in dic:
                dic[node.left] = l
            if node.right not in dic:
                dic[node.right] = r
            ans = max(l, r) + 1
            dic[node] = ans
            return ans

        depth(root)
        diameter = 0

        def traversal(node: Optional[TreeNode]):
            nonlocal diameter
            if not node:
                return
            tmp = dic[node.left] + dic[node.right]
            diameter = max(tmp, diameter)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return diameter

root = createTree([1,2,3,4,5])
solution = Solution()
ans = solution.diameterOfBinaryTree(root)
print(ans)