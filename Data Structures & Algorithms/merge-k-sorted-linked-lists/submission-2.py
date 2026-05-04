# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge lists one by one then
        # O(n*k) where k is the number of lists and n is all elements


        # k pointers approach: also O(n*k)
        # initialize k pointers (a pointer for each list)
        # get the min value of all the pointers and advance the pointer when adding the min for that
        # since we're making a new linkedlist and adding that we can do it like this

        # initialize pointers
        dummyNode = ListNode()
        curNode = dummyNode

        while True:
            minIndex = -1
            minVal = None # if its -1 then finish and break out
            # iterate through the pointers
            for i,node in enumerate(lists):
                if node is None:
                    continue
                if minIndex == -1:
                    minVal = node.val
                    minIndex = i
                else:
                    if minVal > node.val:
                        minVal = node.val
                        minIndex = i
            if minIndex == -1:
                break
            #else then we can continue: set curNode.next to next vlaue and advance both pointers
            curNode.next = ListNode(minVal)

            curNode = curNode.next
            lists[minIndex] = lists[minIndex].next
                



        return dummyNode.next