class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    def addNode(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.tail
    def removeNode(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addNode(node)
            return
        node = Node(key, value)
        self.addNode(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.removeNode(lru)
            del self.cache[lru.key]







