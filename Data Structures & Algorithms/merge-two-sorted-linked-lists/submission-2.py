# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # they're sorted so just iterate thru them and compare

        curNode1,curNode2 = list1,list2
        res = ListNode()
        curNode = res

        while curNode1 and curNode2:
            if curNode1.val < curNode2.val:
                newNode = ListNode(curNode1.val)
                curNode.next = newNode
                curNode1 = curNode1.next
            else:
                newNode = ListNode(curNode2.val)
                curNode.next = newNode
                curNode2 = curNode2.next
            
            curNode = curNode.next
        while curNode1:
            newNode = ListNode(curNode1.val)
            curNode.next = newNode
            curNode1 = curNode1.next
            curNode = curNode.next

        while curNode2:
            newNode = ListNode(curNode2.val)
            curNode.next = newNode
            curNode2 = curNode2.next
            curNode = curNode.next
        
        return res.next




                