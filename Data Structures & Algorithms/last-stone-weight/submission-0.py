class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,3,6,2,4]
        # reorder around 
        # use heap structure
        # call heapify on stones initially
        # grab the two largest elements 

        # perform smashing
        # if == then remove both elements from stones and call heapify
        # if y > x, y = y-x call heapify at 

        # when you call pop() or push it automatically heapify's itself O(logn)
        max_heap = [-1 * val for val in stones]
        
        heapq.heapify(max_heap) # O(n) made stones into a heap
        

        while len(max_heap) > 1:
            print(max_heap)
        # get teh 2 largest values
            l1 = -heapq.heappop(max_heap) # logn
            l2 = -heapq.heappop(max_heap) # log n
            # do some comparisons on them
            if l1 > l2:
                l1 = l1 - l2
                heapq.heappush(max_heap,-l1)
        
        
        # length of the heap could be 0 or 1
        if len(max_heap) == 1:
            return -max_heap[0]
        return 0
