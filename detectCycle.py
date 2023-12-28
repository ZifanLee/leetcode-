from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSet = set()
        while head:
            if head in nodeSet:
                return head
            nodeSet.add(head)
            head = head.next
        return None
