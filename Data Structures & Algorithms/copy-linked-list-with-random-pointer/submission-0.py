"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # each node has, val, randompointer, next
        # random pointer is stored as an index
        # we want to create deep copy a linkedlist
        # 
        if not head:
            return None

        # two-pass

        # first pass
        # ignores random pointer
        # make a deep copy as normal and set random to null for now
        # create a hashmap with pointer as our key
        # and the value stored is the corrosponding pointer created for that original pointer

        # 3,7,4,5,null
        # 3(random = null),7(ranodom),4,5,null

        # [Node(3), Node(3), Node(5), Node(5)]

        # 2nd pass that deals with random
        # since we've already created a key value pair for EACH nodei n the thing, we just need to replace null
        # with the key value pair that goes there (if its not null)

        # 3(null), 7(5), 
        map = {} # key is going to be a Node and the Value is also a node
        # first pass
        newHead = Node(head.val)
        map[head] = newHead # update reference
        curNew = newHead
        # iterate thru the old head nad update newHead
        curOld = head
        while curOld:
            if curOld.next:
                curNew.next = Node(curOld.next.val)
                # update eference
                map[curOld.next] = curNew.next
            # advance pointers
            curNew = curNew.next
            curOld = curOld.next
        
        # self.print_linked_list(newHead)
        # 2nd pass for randoms
        curOld = head
        curNew = newHead
        while curOld:
            if curOld.random:
                # print("procced for " + str(curNew.val))
                # it points to something
                nodeToPointTo = map.get(curOld.random)
                curNew.random = nodeToPointTo
            curOld = curOld.next
            curNew = curNew.next
        return newHead

            
            


    def print_linked_list(self, head: Node) -> None:
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")




