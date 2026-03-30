class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return an array with the max element of each window?

        # [1,2,1,0,4,2,6]

        # find the maximum of each fixed window
        # store it into an array and return that

        # what are we optimizing for?
        # are we guarunteed the input is always valid?

        # Brute force solution: O(n * k) iterate through the array with a sliding window 
        # each window iterate through the windowto find the maximum

        # use a data structure to get the max value faster
        # heappush, heappop are all O(logk) where k is the size of the input array

        # to transform an array to heap initially it is O(k) but since we're only doing this once it doesn't really matter

        # create a window subarray: heappify it (change it into a heap)

        # everytime we add a new element we can add it to the heap with its value and index (value,index)

        # when finding the maximum, discard all values that aren't the within the bounds (call pop)

        res = []
        curHeap = []
        # left and right pointers for sliding iwndow
        left = 0
        for right in range(0, len(nums)):
        # create the initial heap of fixed window
            if right < k:
                entry = (-nums[right], right)
                heapq.heappush(curHeap, entry)
                if right == k-1:
                    # get the max value and add it toeh res
                    res.append(-curHeap[0][0])
            else:
                # dealing with fully fixed window
                # 'remove' the last element
                left += 1
                # add the new element to the heap
                entry = (-nums[right], right)
                heapq.heappush(curHeap, entry)

                # get the max value and append to result (first discard any values with the wrog index)
                topEntry = curHeap[0]
                while topEntry[1] < left:
                    # get next value (pop it off)
                    heapq.heappop(curHeap)
                    topEntry = curHeap[0]
                # add this element to the result
                res.append(-curHeap[0][0])
        return res 

        # 

