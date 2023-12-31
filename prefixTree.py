class TrieNode:
    def __init__(self, value=''):
        self.isEnd = False
        self.next = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.next:
                ptr.next[char] = TrieNode()
            ptr = ptr.next[char]
        ptr.isEnd = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            if char not in ptr.next:
                return False
            ptr = ptr.next[char]
        return ptr.isEnd


    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.next:
                return False
            ptr = ptr.next[char]
        return True