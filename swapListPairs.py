from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = ListNode(1)
        pre.next = head
        ans = pre
        first = head
        second = head.next
        after = head.next.next
        while second:
            pre.next = second
            second.next = first
            first.next = after

            pre = first
            first = after
            if first:
                second = first.next
            else:
                second = None
            if second:
                after = second.next
            else:
                after = None
        return ans.next

