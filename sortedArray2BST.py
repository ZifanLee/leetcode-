from typing import Optional, List
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(nums: List[int], begin: int, end: int) -> Optional[TreeNode]:
            if begin < 0 or end >= len(nums) or begin > end:
                return None
            if begin == end:
                return TreeNode(nums[begin])
            med = int((begin + end)/2)
            root = TreeNode(nums[med])
            root.left = convert(nums, begin, med - 1)
            root.right = convert(nums, med + 1, end)
            return root

        return convert(nums, 0, len(nums) - 1)
