from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        nodes = []
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        if n == len(nodes):
            return head.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-(n+1)].next = nodes[-(n-1)]
        return head
