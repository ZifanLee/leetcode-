from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        ptrA, ptrB = list1, list2
        newHead = ListNode()
        begin = newHead
        while ptrA and ptrB:
            if ptrA.val <= ptrB.val:
                newHead.next = ptrA
                ptrA = ptrA.next
                newHead = newHead.next
            else:
                newHead.next = ptrB
                ptrB = ptrB.next
                newHead = newHead.next
        newHead.next = ptrA if ptrA else ptrB
        return begin.next
