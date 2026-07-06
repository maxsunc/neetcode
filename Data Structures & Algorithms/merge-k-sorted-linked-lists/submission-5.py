# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force:
        # have a pointer for each list and find the minimium of each pointer and append that one

        # O (N * k) : k = number of list, N = total number of nodes
        
        # O(N * logk)

        # minHeap: have a pointer for each linkedList:
        # append them to a heap:
        # pop the minmium element from the heap and put to our result list
        # advance that pointer and add to the list if the pointer isnt None

        heap = [] # store (value, node)
        count = 0
        for node in lists:
            if not node:
                continue
            entry = (node.val, count, node)
            count += 1
            heapq.heappush(heap, entry)
        dummyNode = ListNode()
        curNode = dummyNode

        while heap:
            entry = heapq.heappop(heap)
            curNode.next = ListNode(entry[0])

            curNode = curNode.next

            # advance the entrty[1]
            next = entry[2].next
            if next:
                newEntry = (next.val,count, next)
                count += 1
                heapq.heappush(heap,newEntry)  

        return dummyNode.next

