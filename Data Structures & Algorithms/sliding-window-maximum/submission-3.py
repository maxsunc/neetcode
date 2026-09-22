class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # find the max sliding window of EACH position

        # strictly increasing result


        # use a fixed sliding window

        # find the sum of it. 

        # when we move the lsiding window: add the next value and subtract the old value

        # do this until we reach the end

        # keep track of the max sliding window found

        # if our curSum beats it replace it
        # each window iteration add to the result

        # O(nlogn)
        if k <= 0:
            return []
        left = 0
        heap = []
        res = []

        for right in range(0, len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            
            if right - left + 1 >= k:
                # is the top value of the heap index within right to left?
                # print(heap)
                while (heap[0][1] < left or heap[0][1] > right):
                    # pop off
                    heapq.heappop(heap)
                res.append(-heap[0][0])
                # move the left pointer up and reduce the value
                left += 1
        return res

