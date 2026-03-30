# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a new in place

        # 0 - 1 - 2 - 3

        # 0 <- 1

        cur, prev = head, None


        while cur:
            next = cur.next

            # point curNode to prev
            cur.next = prev

            prev = cur
            cur = next
        return prev
