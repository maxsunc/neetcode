# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # the other merging solution O(n * k)
        heap = []
        # heap solution
        # put all ListNodes into a heap by tuple of (value, node)
        count = 0
        for l in lists:
            # entry = 
            heapq.heappush(heap, (l.val, count, l))
            count += 1

        # O(nlogk)
        # phase 2: take off the top
        res = ListNode()
        head = res
        while heap:
            entry = heapq.heappop(heap)
            # add it to the result as a new node
            res.next = ListNode(entry[0])
            # advance to the next leement
            next = entry[2].next
            if next:
                entry = (next.val, entry[1], next)
                heapq.heappush(heap, entry)
            # advance
            res = res.next
        return head.next


        #O(nlogk)