# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two linked lists we want to make a new one and return it, keep it sorted

        # list1 and list2 are always sorted?
        # always valid input?

        # edge cases: can list1 and list2 be nothing

        # make a linkedlist node 
        dummyNode = ListNode()
        curNode = dummyNode
        
        while list1 and list2:
            # both exist so we c an compare whjich one to add
            if list1.val > list2.val:
                curNode.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curNode.next = ListNode(list1.val)
                list1 = list1.next
            curNode = curNode.next
        while list1:
            curNode.next = ListNode(list1.val)
            list1 = list1.next
            curNode = curNode.next

        while list2:
            curNode.next = ListNode(list2.val)
            list2 = list2.next
            curNode = curNode.next
        return dummyNode.next

