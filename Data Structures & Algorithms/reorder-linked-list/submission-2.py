# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       
        # STEP 1 FIND the size of the array n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        def reverse(node):
            # given a node reverse the linkedlist
            prev = None
            cur = node
            while cur:
                next = cur.next

                # make cur point to prev
                cur.next = prev

                prev = cur
                cur = next
            return prev
        def printNode(node):
            cur = node
            while cur:
                print(cur.val)
                cur = cur.next
            

        # step 2 reverse the partitioned array starting from n // 2 to n
        secondHalf = head
        # go to the middle half
        for i in range(0, n // 2):
            if i == (n // 2) - 1:
                oldNext = secondHalf.next
                secondHalf.next = None
                secondHalf = oldNext
            else:
                secondHalf = secondHalf.next
        # reverse and save the node of the reversed head
        second = reverse(secondHalf)
        # printNode(second)
        cur = head
        finalSecond = None
        # iterate through the linkedlist 
        while cur:
            # print(cur.val)
            # print(second.val)
            # save the old next to traverse later for both
            oldNext = cur.next
            if not oldNext:
                # next is null
                finalSecond = second
            oldSecondNext = second.next

            # make the next of cur to second
            cur.next = second
            second.next = oldNext

            # advance both pointers
            cur = oldNext
            second = oldSecondNext
        # somehow save the final element
        if finalSecond:
            finalSecond.next = second

        # [1,2]
        # [5,4,3]
        # [1-->5-->2-->4-->None]


