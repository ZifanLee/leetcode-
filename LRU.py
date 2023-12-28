class Node:
    def __init__(self, val=0, key=0, pre=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.head = Node(0)
        self.end = Node(0)
        self.head.next = self.end
        self.end.pre = self.head
        self.nodeDic = {}

    def get(self, key: int) -> int:
        if key in self.nodeDic:
            ans = self.nodeDic[key].val
            node = self.nodeDic[key]
            node.pre.next = node.next
            node.next.pre = node.pre

            tmp = self.head.next
            node.pre = self.head
            node.next = tmp
            self.head.next = node
            tmp.pre = node
        else:
            return -1
        return ans

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeDic:
            if self.capacity == self.cnt:
                tmp = self.end.pre
                tmp.pre.next = self.end
                self.end.pre = tmp.pre
                self.cnt -= 1
                self.nodeDic.pop(tmp.key)
            node = Node(value, key)
            self.nodeDic[key] = node
            st = self.head.next
            node.pre = self.head
            self.head.next = node
            node.next = st
            st.pre = node
            self.cnt += 1
        else:
            node = self.nodeDic[key]
            node.val = value
            node.pre.next = node.next
            node.next.pre = node.pre
            st = self.head.next
            node.pre = self.head
            self.head.next = node
            node.next = st
            st.pre = node



