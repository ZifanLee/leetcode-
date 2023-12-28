from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodelist = []
        while head:
            nodelist.append(head.val)
            head = head.next
        i, j =0, len(nodelist)-1
        while i <= j:
            if nodelist[i] != nodelist[j]:
                return False
            i += 1
            j -= 1
        return True
