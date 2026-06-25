# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        curNode = head
        while curNode:
            if curNode in seen:
                return True
            seen.add(curNode)
            curNode = curNode.next
        return False