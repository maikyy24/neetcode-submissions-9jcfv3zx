class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insert(newNode)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev = self.left
        nxt = self.left.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node