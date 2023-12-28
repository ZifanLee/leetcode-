from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        nodeSet = set()
        while A:
            nodeSet.add(A)
            A = A.next
        while B:
            if B in nodeSet:
                return B
            B = B.next
        return None
