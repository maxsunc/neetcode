class MedianFinder:

    def __init__(self):
        # find the median from a data stream
        # Easiest solution maintain a sorted list
        # addNum is O(n), findMedina is O(1) a bit slow..

        # Optimal Solution: O(logn) for addNum
        # O(1) for findMedian: 
        # Min heap: 

        # 

        #[1,3,2]
        # split the 2ends and find the 

        # use 2 heaps
        # min heap and max heap
        # keep them equal

        # sorted
        # 1,2,4,6,7

        # smallheap = 4,2,1 (maxHeap)
        # largeHeap = 6,7,9  (minHeap) # 6 = min element if anything is less than this, it goes to the smallHeap

        self.smallHeap = []
        self.largeHeap = [] # min heap to get the min element from here


    def addNum(self, num: int) -> None:
        print(f"adding {num} onto {self.smallHeap}{self.largeHeap}")
        if not self.largeHeap:
            heapq.heappush(self.largeHeap, num)
            return
        
        # push the value onto the max Heap if it is less than the min heap
        if self.largeHeap[0] > num:
            heapq.heappush(self.smallHeap, -num)
        else:
            heapq.heappush(self.largeHeap,num)

        # check and equalize the sizes
        if (len(self.largeHeap) + len(self.smallHeap)) % 2 == 0:
            # even it out we if we can
            while len(self.largeHeap) > len(self.smallHeap):
                element = heapq.heappop(self.largeHeap)
                heapq.heappush(self.smallHeap, -element)
            while len(self.smallHeap) > len(self.largeHeap):
                element = -heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap, element)



    def findMedian(self) -> float:
        # returns the median of the current elements
        # only called after adding at least one integer to the data structure
        # split the array, find the max of the ley side and the min of the right side
        totalLength = len(self.largeHeap) + len(self.smallHeap)
        
        # case 1: Even length. Get the max from the smallHeap and the min from the largeHeap and average them
        if totalLength % 2 == 0:
            # get the min and max and average
            return (self.largeHeap[0] + -self.smallHeap[0]) / 2
        else:
        # case 2: take the min/max from the bigger array
            return self.largeHeap[0] if len(self.largeHeap) > len(self.smallHeap) else -self.smallHeap[0]

        