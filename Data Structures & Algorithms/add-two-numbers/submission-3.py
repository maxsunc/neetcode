# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res
        carryOne = 0
        while l1 and l2:
            summed = l1.val + l2.val + carryOne

            if summed >= 10:
                summed -= 10
                carryOne = 1
            else:
                carryOne = 0
            # add it to res
            cur.next = ListNode(summed)
            
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            summed = l1.val + carryOne
            if summed >= 10:
                summed -= 10
                carryOne = 1
            else:
                carryOne = 0
            cur.next = ListNode(summed)
            cur = cur.next
            l1 = l1.next
        while l2:
            summed = l2.val + carryOne
            
            if summed >= 10:
                summed -= 10
                carryOne = 1
            else:
                carryOne = 0
            cur.next = ListNode(summed)
            cur = cur.next
            l2 = l2.next
        if carryOne:
            cur.next = ListNode(carryOne)
        return res.next
        # return the reversed