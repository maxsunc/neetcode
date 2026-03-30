# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        root = None
        if list1 == None and list2 == None:
            return root
        if list1 == None:
            node = ListNode(list2.val)
            root = node
            list2 = list2.next
            while list2 != None:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
            
            return root
        elif list2 == None:
            node = ListNode(list1.val)
            root = node
            list1 = list1.next
            while list1 != None:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next

            return root


        # initialize
        if list1.val > list2.val:
            node = ListNode(list2.val)
            root = node
            list2 = list2.next
        else:
            node = ListNode(list1.val)
            root = node
            list1 = list1.next
        
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
            else:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next

        while list1 != None:
            node.next = ListNode(list1.val)
            node = node.next
            list1 = list1.next

        while list2 != None:
            node.next = ListNode(list2.val)
            node = node.next
            list2 = list2.next
        
        return root

        
            