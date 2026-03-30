class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        # we made a heap with the values I think we're goood..
        for i in nums:
            self.add(i)
    def add(self, val: int) -> int:
        # we're never going to remove values, this means any values less than kth largest is uselss
        # we don't even need to add them
        # maintain only k elements
        if len(self.minHeap) < self.k:
            # add it for free
            heapq.heappush(self.minHeap, val)# push it to the correct position
        # now we know we're of length 
        # check if the smallest value is less than val
        elif self.minHeap[0] < val:
            # it passes the MINIMUM requirements
            heapq.heappushpop(self.minHeap, val) # pops the value then pushes
        # returns the kth largest which is our smallest value of a minheap, genius
        return self.minHeap[0] 
        