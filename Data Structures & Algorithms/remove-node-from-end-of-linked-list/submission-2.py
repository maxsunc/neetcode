# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove the nth node from the end of the list and return its head


        # could do it in 2 passes


        # we first need to find the length fo the linked list

        # [1,2,3,4]

        # 1. get the length of the list
        curNode = head

        length = 0
        while curNode:
            length += 1
            curNode = curNode.next


        # 2. convert the nth node from the end to node from the start
        m = length - n
        # count up to node and delete that node
        # special case: if the deleting node is the front node then just return the next node
        if m == 0:
            return head.next
        # normal case where we go and delete a node
        curNode = head
        prev = None
        for i in range(0, m ):
            prev = curNode
            curNode = curNode.next
        # delete it
        print(f"{prev} and {curNode}")
        prev.next = curNode.next
        # return the head
        return head


