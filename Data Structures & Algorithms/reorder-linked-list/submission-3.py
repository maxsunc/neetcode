# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # keep track of the nodes by indicies in a map or hashmap or something
        # find n also (length of hte linkedlist)
        # keep a ref to every node by that



        # iterate from 0 to n - 1 inclusive:
        # keep track of a curNode that starts at head.

        # for each i from 1 to n inclusive
        # set the next of curNode to n-1
        # advance curNode
        # then set the next of curNode to 1 if possible and it does match n-1
        # 

        indexToNodes = {}
        curIndex = 0
        curNode = head
        while curNode:
            indexToNodes[curIndex] = curNode
            curIndex += 1
            curNode = curNode.next
        n = curIndex
        # 2nd pass: replacement phase
        curNode = head

        for i in range(1,1 + n//2):
            curNode.next = indexToNodes[n-i]
            curNode = curNode.next
            if n - i != i:
                curNode.next = indexToNodes[i]
                curNode = curNode.next
        curNode.next = None



