class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Store k as an instance variable
        self.k = k
        # Create a min heap with at most k largest elements
        self.minHeap = []
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        # If heap has fewer than k elements, just add
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        # If val is larger than smallest element in heap, replace smallest
        elif val > self.minHeap[0]:
            heapq.heappushpop(self.minHeap, val)
        
        # Return the kth largest (smallest element in our min-heap)
        return self.minHeap[0]