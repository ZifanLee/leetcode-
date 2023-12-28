from typing import Optional, List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = Queue(maxsize=0)
        q.put(root)
        while not q.empty():
            cnt = q.qsize()
            for i in range(cnt-1):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            node = q.get()
            ans.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return ans