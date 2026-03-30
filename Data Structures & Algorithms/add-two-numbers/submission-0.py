# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # [1,2,4]  [4,5,6,7,8]
        # keep track of carry one for each digit point
        # iterate until BOTH iterators are None
        # when both are none we stop
        # keep track of our result which is a linkedlist aswell
        # O(n) time complexity
        # O(1) 

        # 
        curNode1 = l1
        curNode2 = l2
        carryOut = 0
        sum = curNode1.val + curNode2.val
        if sum >= 10:
            sum -= 10
            carryOut = 1
        else:
            carryOut = 0

        head = ListNode(sum)
        curNode = head
        curNode1 = curNode1.next
        curNode2 = curNode2.next
        while curNode1 or curNode2:
            sum = 0
            if curNode1:
                sum += curNode1.val
                curNode1 = curNode1.next
            if curNode2:
                sum += curNode2.val
                curNode2 = curNode2.next
            sum += carryOut
            if sum >= 10:
                sum -= 10
                carryOut = 1
            else:
                carryOut = 0
            curNode.next = ListNode(sum)

            
            
            curNode = curNode.next
        # case for carryout = 1 after going through all place
        if carryOut == 1:
            curNode.next = ListNode(1)
        
        return head
        # 1. iterate through the max length of the linkedlist
        
        # 2. dont look thru any iterators if its null

        # add both the values AND carry one,, (subtract 10 AND set carry out to one if >= 10 else set carry out to 0)

        # 3. update our curNode at the result to the sum % 10 

        # 4. advance each iterators (result, curNode1, curNode2,), set the carryOut

        # 5. return the result

        return None
        

