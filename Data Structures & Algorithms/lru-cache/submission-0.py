class Node:
    def __init__(self,key:int,value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        prev = node.prev
        nxt = node.next 

        nxt.prev = prev
        prev.next = nxt

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        prev.next = node

        node.next = nxt
        nxt.prev = node 

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
