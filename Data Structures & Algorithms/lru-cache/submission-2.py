class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = -1
        self.mru = -1
        self.keyToPointer = {}
        self.n = capacity
        self.cache = {}

    def addRecentlyUsed(self, key):
        if self.lru == -1:
            self.keyToPointer[key] = Node(key)
            self.lru = key
            self.mru = key
            return
        
        if self.mru == key:
            return
        
        if key in self.keyToPointer:
            if key == self.lru and self.keyToPointer[self.lru].next:
                self.lru = self.keyToPointer[self.lru].next.val
            
            head = self.keyToPointer.get(self.mru)
            curNode = self.keyToPointer.get(key)
            if curNode.prev:
                curNode.prev.next = curNode.next
            if curNode.next:
                curNode.next.prev = curNode.prev
            head.next = curNode
            curNode.prev = head
            curNode.next = None  # FIX: Set next to None when moving to MRU
            self.mru = key
        else:
            head = self.keyToPointer.get(self.mru)
            self.keyToPointer[key] = Node(key)
            head.next = self.keyToPointer[key]
            self.keyToPointer[key].prev = head
            self.mru = key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.addRecentlyUsed(key)  # FIX: Move after the check
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # FIX: Check if key already exists
        if key in self.cache:
            self.cache[key] = value
            self.addRecentlyUsed(key)
            return
        
        if len(self.cache) >= self.n:
            oldLru = self.lru
            # FIX: Handle case where next is None
            if self.keyToPointer[self.lru].next:
                self.lru = self.keyToPointer[self.lru].next.val
                self.keyToPointer[self.lru].prev = None  # FIX: Remove dangling pointer
            else:
                # Only one element, will be replaced
                self.lru = -1
                self.mru = -1
            
            self.cache.pop(oldLru)
            self.keyToPointer.pop(oldLru)
        
        self.cache[key] = value
        self.addRecentlyUsed(key)