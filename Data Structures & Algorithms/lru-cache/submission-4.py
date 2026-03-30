class LRUCache:

    def __init__(self, capacity: int):
        # how to keep track fo the least recently used element?
        # we need ot make use of a data structure

        # we could use a doubly linkedlist since removing elements from it is O(1) time 
        # and O(1) time to repair

        #to access the node fast we can make use a of dictionary from (key) int to Node

        # initialize the LRU cache of size capacity
        # key is used if get or put is called on it
        #
        # get and put is O(1) speed
        self.capacity = capacity
        # need a dictionary pointing from key to node
        self.map = {}
        self.top = None
        self.bottom = None

    def get(self, key: int) -> int:
        # return the value corrosponding to the key or just -1
        node = self.map.get(key, None)
        if not node:
            return -1
        # update the recency ( we have access to the Node so move it to the top (set the bwd of the current top to this thn set top = bwd))

        # [a<-->b<-->c-->d]
        # [b-->a-->c-->d]

        # 1: remove the bwd pointer of the front element

                
        # 2: remove the fwd point of the back element
        self.markUsed(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        # case 1: Update the key with value
        if key in self.map:
            self.map[key].val = value
            self.markUsed(self.map[key]) # mark the node as used
        # case 2: add a key value pair to the cache
        else:
        # case 2.1: Cache is below capacity, add it as usual
            if len(self.map) >= self.capacity:
                print(self.map)
                print(self.bottom)
                # evict the least used capacity
                nodeEvict = self.bottom
                self.bottom = self.bottom.bwd
                # self.bottom = None # dont point anymore (prolly not neeeded)
                # remove the key at bottom
                keyEvict = nodeEvict.key
                self.map.pop(keyEvict)


                # add it as a new element thats fine
            self.map[key] = Node(key, value, None, None)
            self.markUsed(self.map[key])
        # case 2.2: Cache is above capacity evict the least recently used element and put this element in place of that element
    
    def markUsed(self, node):
        if node is self.top:
            return  # already most recent, nothing to do

        # Update bottom pointer if this node is being pulled from the end
        if node is self.bottom and node.bwd:
            self.bottom = node.bwd

        # Stitch neighbours together
        if node.fwd:
            node.fwd.bwd = node.bwd
        if node.bwd:
            node.bwd.fwd = node.fwd

        # Place node at top
        node.bwd = None
        node.fwd = self.top
        if self.top:
            self.top.bwd = node
        self.top = node

        # First element ever added
        if not self.bottom:
            self.bottom = node
class Node:
    def __init__(self, key, val, fwd = None, bwd = None):
        self.key = key
        self.val = val
        self.fwd = fwd
        self.bwd = bwd
