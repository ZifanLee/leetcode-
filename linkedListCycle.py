from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        move = False
        while fast:
            if fast == slow:
                return True
            fast = fast.next
            if move:
                slow = slow.next
                move = False
            else:
                move = True
        return False

