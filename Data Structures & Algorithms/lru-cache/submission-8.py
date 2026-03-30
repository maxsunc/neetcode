class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.first = None
        self.last = None
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.markUsed(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.markUsed(self.map[key])
            return
        else:
            if self.cap <= len(self.map):
                keyToRemove = self.last.key
                self.map.pop(keyToRemove)
                self.last = self.last.back
                if self.last:
                    self.last.next = None

            node = ListNode(key, value, None, None)
            self.markUsed(node)
            self.map[key] = node

    def markUsed(self, node):
        if self.first == node:
            return

        # Promote existing last pointer
        if self.last == node and node.back:
            self.last = node.back
            self.last.next = None

        if node.key not in self.map:
            # New node: just prepend
            node.next = self.first
            if self.first:
                self.first.back = node
            if not self.last:      # was empty
                self.last = node
            elif self.first == self.last:  # had one element, node is new last... 
                pass               # self.last already correct (still points to old first)
        else:
            # Existing node: stitch neighbours then prepend
            if node.next:
                node.next.back = node.back
            if node.back:
                node.back.next = node.next
            node.back = None
            node.next = self.first
            if self.first:
                self.first.back = node

        self.first = node


class ListNode:
    def __init__(self, key, val, next=None, back=None):
        self.key = key
        self.val = val
        self.next = next
        self.back = back