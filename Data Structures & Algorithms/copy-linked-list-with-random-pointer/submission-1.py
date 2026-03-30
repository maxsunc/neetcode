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
        # create a deeo cioy 
        # Isi t possible to make a dictionary with the key being a node?
        map = {}

        # store original --> copy for each new Node encountered
        dummyCopy = Node(0)

        # first pass create each node and the next of each node
        cur = head
        curCopy = dummyCopy
        while cur:
            # create a next entry with the copy as the vlaue
            map[cur] = Node(cur.val)
            curCopy.next = map[cur]

            #[0 --> 1 --> ]

            cur = cur.next
            curCopy = curCopy.next

        # iterate through both again now pay fill in the random elements now that we have each original to copy stored
        cur = head
        curCopy = dummyCopy.next
        while cur:
            rndNode = cur.random
            curCopy.random = map.get(rndNode, None)

            cur = cur.next
            curCopy = curCopy.next
        return dummyCopy.next


        # 2nd pass, fill in the random values