from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        index1, index2 = 0, 0
        digit = 0
        result = []
        while index1 < len(num1) and index2 < len(num2):
            digit += num1[index1] + num2[index2]
            result.append(digit%10)
            index1 += 1
            index2 += 1
            if digit >= 10:
                digit = 1
            else:
                digit = 0
        while index1 < len(num1):
            digit += num1[index1]
            result.append(digit % 10)
            index1 += 1
            if digit >= 10:
                digit = 1
            else:
                digit = 0
        while index2 < len(num2):
            digit += num2[index2]
            result.append(digit % 10)
            index2 += 1
            if digit >= 10:
                digit = 1
            else:
                digit = 0
        if digit == 1:
            result.append(digit)

        head = ListNode(0)
        ptr = head
        for num in result:
            node = ListNode(num)
            ptr.next = node
            ptr = ptr.next
        return head.next


def createList(nums: List[int]):
    if not nums:
        return None
    pre = ListNode(0)
    ans = pre
    for num in nums:
        pre.next = ListNode(num)
        pre = pre.next
    return ans.next

solution = Solution()
list1 = createList([2, 4, 9])
list2 = createList([5, 6, 4, 9])
solution.addTwoNumbers(list1, list2)
