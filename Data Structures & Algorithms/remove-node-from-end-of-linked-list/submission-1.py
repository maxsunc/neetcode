# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass

        # pass once to get the size

        # iterate to the nth node and remove it

        # removing the nth node from the end

        # find length of the linkedList

        # convert the node to remove from end to start to start to end (len - n)

        # # remove as normal

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        index = length - n

        cur = head
        prev = None

        for i in range(0, index):
            # go from 0 to index
            
            prev = cur
            cur = cur.next
        
        # delete this node
        #[1,2,3,4,5]
        if prev:
            prev.next = cur.next
        else:
            # we know its the head we're trying to delete
            head = head.next
        return head

