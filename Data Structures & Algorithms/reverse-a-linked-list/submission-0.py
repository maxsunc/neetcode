# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        node = None

        def dfs(nextNode):
            nonlocal newHead, node   # <-- lets inner function assign outer vars

            if nextNode.next is None:
                print('hello')
                newHead = ListNode(nextNode.val)
                node = newHead
                return
            
            dfs(nextNode.next)

            if newHead.next is None:
                node = ListNode(nextNode.val)
                newHead.next = node
            else:
                node.next = ListNode(nextNode.val)
                node = node.next

        if head:
            dfs(head)
        return newHead
