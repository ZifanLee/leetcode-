from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pre = None
        current = head
        after = head.next
        while current:
            current.next = pre
            pre = current
            current = after
            if after:
                after = after.next
        return pre
