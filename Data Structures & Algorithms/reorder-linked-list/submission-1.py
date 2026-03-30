# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # do this inplace with weirs tuff
        # find the middle point
        slow, fast = head, head
        while fast and fast.next: # do it until we reach lasst node (even length), or null (odd length)
            slow = slow.next
            fast = fast.next.next
        # []
        # 8 --> 10
        # 2 --> 4 --> 6 --> none

        # the middle goes from slow.next to fast
        second = slow.next
        print("Second linkedList starts at " + str(second.val))
        # cutoff the first split part
        slow.next = None

        # reverse the 2nd half
        # second half starts at slow.next or (second)
        prev = second.next
        second.next = None
        # 2. 2 <-- 4 --> 5,6,7
        while prev != None:
            nextNode = prev.next
            prev.next = second
            
            second = prev
            
            prev = nextNode
        

        # if second.next != None:
        #     print(second.next.val) # makes no error here
        #3. we have second, and first (head)
        # build out new rearranged linkedlist
        first = head # left pointer
        # 2 --> 4  6 <-- 8
        curNode = head # iterator

        # iterate until both pointers are None
        while second != None and first != None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next if first_next else second  # safe advance
            second = second_next
            
        






        

        # having 2 pointers
        # iterate thru the linkedlist
        # curNode.next = second
        # advance second and curNode

        # curNode.next = first
        # advance first and curNode

        # do this until first and second are null
                

        