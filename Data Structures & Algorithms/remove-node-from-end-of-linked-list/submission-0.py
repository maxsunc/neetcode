# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get tehe length of the linkedlist
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1
        # recalculate an n value
        newN = length - n + 1

        # 1,2,3,4,5
        # n = 2
        # 5 -2 + 1 = 4
        curNode = head
        prev = None
        # advance curNode
        for i in range(1, newN):
            prev = curNode
            curNode = curNode.next
        
        # now delete at curNode
        if prev == None:
            # deleting the first node
            return curNode.next
        # deleting at anywhere else
        prev.next = curNode.next # curNode should never be None right?
        return head