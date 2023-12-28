from typing import Optional
from typing import List
from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    if not head:
        return None, None
    pre = None
    ptr = head
    after = head.next
    end = head
    while ptr:
        ptr.next = pre
        pre = ptr
        ptr = after
        if after:
            after = after.next
    return pre, head


def createList(nums: List[int]):
    if not nums:
        return None
    pre = ListNode(0)
    ans = pre
    for num in nums:
        pre.next = ListNode(num)
        pre = pre.next
    return ans.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        cnt = 1
        tmpbegin = head
        end = head
        nodeList = []
        lastnode = None
        while end:
            while end and cnt < k:
                end = end.next
                cnt += 1
            if not end:
                lastnode = tmpbegin
                break
            nodeList.append(tmpbegin)
            tmpbegin = end.next
            end.next = None
            end = tmpbegin
            cnt = 1
        pre = ListNode(0)
        ptr = pre
        for node in nodeList:
            tmpbegin, tmpend = reverseList(node)
            ptr.next = tmpbegin
            ptr = tmpend
        ptr.next = lastnode
        return pre.next





head = createList([1, 2, 3, 4, 5, 6,7 ,8])
solution = Solution()
head = solution.reverseKGroup(head, 3)
while head:
    print(head.val)
    head = head.next