from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        ptr = head
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next
        ptr = head
        nums.sort()
        for num in nums:
            ptr.val = num
            ptr = ptr.next
        return head