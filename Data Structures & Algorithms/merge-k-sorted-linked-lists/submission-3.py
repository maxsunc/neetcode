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
        # to reduce this to O(nlogk) we can use a minHeap
        # initialize pointers
        dummyNode = ListNode()
        curNode = dummyNode

        # use a minHeap
        # store (val,node)
        # initially iterate thru all and add the first values O(klogk)
        minHeap = []

        # push all the first values onto the minHeap
        count = 0
        for node in lists:
            entry = (node.val,count, node)
            heapq.heappush(minHeap,entry)
            count += 1
        # while loop until the minHeap is empty pop off the minVal and add to curNode,
        # advance the node, if not null, push onto the minHeap
        while minHeap:
            entry = heapq.heappop(minHeap)

            # set the curNode.next to a new value with entry
            curNode.next = ListNode(entry[0])

            curNode = curNode.next
            nextNode = entry[2].next
            if nextNode != None:
                heapq.heappush(minHeap, (nextNode.val,count,nextNode))

                count += 1

                



        return dummyNode.next