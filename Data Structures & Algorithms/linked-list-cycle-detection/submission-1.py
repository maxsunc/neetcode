# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # checking if the list has a cycle or not
        seen = set()
        # traverse through the list, if we encounter a listNode already seen before then return true. If we get to None say false
        curNode = head

        while curNode != None:
            if curNode in seen:
                return True
            seen.add(curNode)
            curNode = curNode.next

        return False
