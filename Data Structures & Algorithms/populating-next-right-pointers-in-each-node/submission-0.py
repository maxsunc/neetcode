"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # what is a perfect tree:
        # is this tree guarunteed to be perfect
        # should we modify the tree in place

        # are next pointer none?

        # Simple: Find the nodes next to each other node and populate the tree with that
        if not root:
            return None
        # curr.left.next = cur.right
        # if this curr has a neighbor to the right:
        # cur.right.next = curr.next.left
        leftmost = root

        # since this is a perfect binary tree: if leftmost.left exists, then this level has children that needs ot be conencted
        while leftmost.left:
            # walk horizontally across current level using next pointers
            curr = leftmost

            while curr:
                # connect the left child to right child
                # connect the left child to the irght child within the same parent
                curr.left.next = curr.right
                
                if curr.next:
                    curr.right.next = curr.next.left
                # move to the next node on the same level
                curr = curr.next
        # move down to the leftmost node of the next level
            leftmost = leftmost.left
        return root


        # 1
        # 2   -> 3
        #4->5->6->7

        # 1: set the left.next = right (if the right and left exists)
        # (if the rigth exists and next exists): 
        # right.next = next.left
        
        # call recursively to traverse 