class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # O(n * m) where m is the longest interval and n is the length of intervals

        # process the intervals in sorted order:
        # sort by start value

        # [[1,3],[2,3],[3,7],[6,6]]

        # [2,3,1,7]

        # [1,2,3,7]
        # using a min heap  with a sorted thing: processs the Query: 
        # 
        # 1. rework the query
        newQuery = []
        for i,num in enumerate(queries):
            newElement = (queries[i], i) # value, original index to add to res
            newQuery.append(newElement)
        newQuery.sort(key=lambda x: x[0])
        # print(f"New Query: {newQuery}")
        # 2. sort intervals by start
        intervals.sort(key=lambda x: x[0])
        # print(f"Intervals {intervals}")
        # keep a min heap to add eleemnts applicable to the minHeap by length 
        minHeap = []
        res = [0 for i in range(0,len(queries))]
        curIndex = 0
        # put the minElement at index

        # iterate thru queries
        for query in newQuery:
            trueInd = query[1]
            n = query[0]
            # print(f"now looking at query {n}")

        # 3. foreach interval in between query element add to the heap
            while curIndex < len(intervals):
                interval = intervals[curIndex]
                if interval[0] <= n:
                    # safely add to the heap
                    element = (interval[1] - interval[0] + 1, interval[1])
                    heapq.heappush(minHeap, element)
                    curIndex += 1
                else:
                    break


        # 4. while the end value of the heapElement is less than the value then pop it off
            while minHeap and minHeap[0][1] < n:
                heapq.heappop(minHeap)
            print(minHeap)
            # print(f"wtf: returning {minHeap[0][0]}")
            res[trueInd] = minHeap[0][0] if minHeap else -1
        return res
        # 5. add it to result

        



        