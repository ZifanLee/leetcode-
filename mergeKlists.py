from typing import Optional
from typing import List
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptr = ListNode(0)
        pre = ptr
        if not lists:
            return None
        lists = [x for x in lists if x]
        while lists:
            minIndex, minNode, minValue = 0, lists[0], lists[0].val
            for index, node in enumerate(lists):
                if node.val < minValue:
                    minIndex = index
                    minValue = node.val
                    minNode = node
            lists[minIndex] = lists[minIndex].next
            if not lists[minIndex]:
                del lists[minIndex]
            ptr.next = minNode
            ptr = ptr.next
        return pre.next



