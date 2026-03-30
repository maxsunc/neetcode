# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        def iterate(node):
            if node == None:
                return False # reached the end

            if node in visited:
                return True # already visited this guy
            else:
                visited.add(node)
                return iterate(node.next)

        return iterate(head)
            
