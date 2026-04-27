class MedianFinder:

    def __init__(self):
        # [1,2,3,4,5] median = 2
        # [1,2] median = (1+2) / 2 = 1.5 (even length)

        # brute force solution: maintain a sorted array: [1,2,4,6] addNum O(N) time
        # find median: O(1): grab the middle value if odd length
        # grab the 2 middle value and average them if even length

        # addNum: O(logn) use 2 heaps
        # lower Heap (maxHeap)
        # upperHeap (minHeap)
        # keep the heaps of mostly the same length: upperHeap can be + 1 length
        # lowerheap must be off by one length or equal length
        self.lowerHeap = [] # maxHeap
        self.upperHeap = [] # minHeap
        self.length = 0




    def addNum(self, num: int) -> None:
        # add to int array
        # [1,2,3]
        # [],[1,2,3]
        # [3],[1]
        if not self.upperHeap:
            heapq.heappush(self.upperHeap,num)
        else:
            if num >= self.upperHeap[0]:
                heapq.heappush(self.upperHeap,num)
            else:
                heapq.heappush(self.lowerHeap,-num)

        # if its greater than orequal to the top value of upper then add to 2nd half
        
        # always add to the top of the uppheap:
        # if the len of the heaps are off by 2 or more pop from upper heap and give to lower heap

        if len(self.upperHeap) > len(self.lowerHeap) + 1:
            val = heapq.heappop(self.upperHeap)
            heapq.heappush(self.lowerHeap,-val)
        elif len(self.upperHeap) < len(self.lowerHeap):
            val = -heapq.heappop(self.lowerHeap)
            heapq.heappush(self.upperHeap,val)
        self.length += 1
        

    def findMedian(self) -> float:
        # return the median of the elements so far

        # if its odd length: take the top element from the heap of upper [0]
        # if its even: take first element from lower heap and upper heap and average them
        median = 0
        if self.length % 2 == 1:
            median = self.upperHeap[0]
            # even:
        else:
            median = (self.upperHeap[0] + -(self.lowerHeap[0])) / 2
        print(f"median form {self.lowerHeap} and {self.upperHeap} is {median}")
        return median



        
        
        