class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # fixed lsiding window
        # find the maximum in each window

        # O(nlogk)

        # use a heap (value, index)
        # when finding the maximum check if the index of the top we're looking at 
        # is within the range from l to r
        # if it is then that is a valid maximum we can put that in and proceed
        # if it isnt we'll need to pop it off to look at the next maximum element

        # we'll be adding elements in one by one too so dw



        l = 0
        curHeap = []
        res = []

        for r in range(0, len(nums)):
            # push to the heap
            heapq.heappush(curHeap, (-nums[r], r))

            # check if our window size is k
            windowSize = r - l+1
            if windowSize == k:
                # print(curHeap)
                # get a maximum value that is with the bounds [l,r]
                maxEntry = curHeap[0]
                # print(f"wtf {maxEntry}")
                while l > maxEntry[1] or r < maxEntry[1]:
                    # print(f"{curHeap} at {l} to {r}")
                    # reroll for a new one
                    heapq.heappop(curHeap)
                    maxEntry = curHeap[0]
                # add this max value 
                res.append(-maxEntry[0])
                # update boundary size 
                l += 1
        
        return res

