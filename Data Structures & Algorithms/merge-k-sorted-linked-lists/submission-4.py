# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curNode = dummyNode

        minHeap = []

        # push all the first values onto the minHeap
        count = 0
        for node in lists:
            if node is None:
                continue
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