# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add two integers 
        # 1-2-3 = 123
        dummy = ListNode()
        curNode = dummy
        carry1 = 0
        # add two values and take the carry one to the next dude
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            val += carry1
            carry1 = 0
            if val >= 10:
                print(val)
                val -= 10
                carry1 = 1
            
            newNode = ListNode(val)
            curNode.next = newNode


            curNode = curNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry1:
            # if the carry1 is 1, then we need to make a new node
            curNode.next = ListNode(1)

        return dummy.next