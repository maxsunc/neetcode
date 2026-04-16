# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # traverse thru a linked lit but keep track ofseen nodes, if the next is aleady seen return false immediantly

        seen = set()
        curNode = head
        while curNode:
            if curNode in seen:
                return True
            # mark as seen
            seen.add(curNode)

            curNode = curNode.next
        return False