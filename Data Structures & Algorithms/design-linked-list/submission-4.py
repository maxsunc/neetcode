class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev



class MyLinkedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        # traverse the linkedlist until we get to index O(N)
        curNode = self.head
        for i in range(0, index):
            curNode = curNode.next
        return curNode.val

        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        # O(1) replace the head
        if self.length == 0:
            
            self.head = newNode
            self.end = newNode
        else:
            # make a newnode and point it to the current head and point the current back to the newNode
            newNode.next = self.head
            self.head.prev = newNode
            # replace the head
            self.head = newNode
        self.length += 1

        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        # replace the end O(1)
        if self.length == 0:
            self.head = newNode
            self.end = newNode
            
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        # O(N): 0
        # edge case: index = 0: call add at head
        # iterate up to index: keep track of the prevSeen node: insert the node after that prevnode
        # 
        if index == 0:
            self.addAtHead(val)
            return
        prev,curNode = None, self.head
        for i in range(0, index):
            if not curNode:
                return # we're oging out of bounds
            # [1,2]
            prev = curNode
            curNode = curNode.next
        # [1,2,3,4,None]
        if not curNode:
            self.addAtTail(val)
            return
        # [1,2]
        newNode = ListNode(val)
        prev.next = newNode
        curNode.prev = newNode
        # point newNodes stuff over
        newNode.prev = prev
        newNode.next = curNode
        self.length += 1

        # [1,2,3,4]
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        # edge cases: deleting head or tail
        # keep track of two nodes
        # iterate until we hit the indexth node
        # [0,1,2,3,4]
        # guarunteed there is 1+ values here
        # edge cases: deleting at head: deleting at end
        if index == 0:
            self.head = self.head.next
        elif index == self.length - 1:
            self.end = self.end.prev
        else:
            # general case where we iterate to find the indexth value
            # guarunteed the indexth value has a next and prev
            curNode = self.head
            for i in range(0, index):
                curNode = curNode.next
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.end = None
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)