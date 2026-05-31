class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = dict()
        self.capacity = capacity

    def insertRight(self, node):
        right, prev = self.right, self.right.prev
        prev.next, right.prev = node, node
        node.prev, node.next = prev, right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertRight(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        newNode = Node(key,value)
        self.cache[key] = newNode
        self.insertRight(newNode)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)