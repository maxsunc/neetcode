class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # make a new list
        # res = []
        # non in place solution
        res = []
        prev = [-1,-1]
        tooBig = True
        def overlap(interval): # returns if it overlaps with newInterval
            nonlocal tooBig
            # [6,7] [5,11] case interval within new interval
            # [4,6] [5,11] case new interval within interval
            # if either values of new interval are within the 
            # [1,2] [6,7]
            if interval[0] <= newInterval[0] <= interval[1] or (interval[0] <= newInterval[1] <= interval[1]) or (newInterval[0] <= interval[0] <= newInterval[1]) or (newInterval[0] <= interval[1] <= newInterval[1]):
                print(f"{newInterval} overlaps with {interval}")
                return True
            # determine whether interval is too big or too small
            if interval[0] > newInterval[1]:
                tooBig = True
            else:
                tooBig = False
            return False
        # if it overlaps update the result
        added = False
        for interval in intervals:
            if not overlap(interval):
                # if the curInterval is bigger than us and prev is smaller
                # if prev[1] <= newInterval[0] and newInterval[1] <= interval[0]:
                #     intervals.append(newInterval)
                if tooBig and not added:
                    added = True
                    res.append(newInterval)
                res.append(interval)
                print("hi")
            else:
                # update new interval with the merged
                newInterval = (min(interval[0],newInterval[0]), max(interval[1],newInterval[1]))
            prev = interval
        if not added:
            res.append(newInterval)
        print(newInterval)

        return res







        # start, end = -1,-1
        # for i,interval in enumerate(intervals):
        #     # get the max positions where newInterval[0] and newInterval[1] belong
        #     if interval[0] <= newInterval[0]:
        #         start = i
        #     if interval[0] <= newInterval[1]:
        #         end = i
        # # merge rom start to end inclusive
        # def removeRedundant(i):
        #     comp = intervals[i]
        #     popList = []
        #     for j, interval in enumerate(intervals):
        #         if j == i:
        #             continue
        #         # absorb if overlapping OR adjacent, not just fully contained
        #         if interval[0] <= comp[1] and interval[1] >= comp[0]:
        #             comp[0] = min(comp[0], interval[0])
        #             comp[1] = max(comp[1], interval[1])
        #             popList.append(j)
        #     intervals[i] = comp
        #     # pop in reverse so indices don't shift
        #     for j in sorted(popList, reverse=True):
        #         intervals.pop(j)


        # # case we need to make a new interval: newINterval[0] isnt within start interval
        # if start == -1:
        #     # insert at the start we're done
        #     intervals.insert(0, newInterval) # edge case
        #     return intervals
        # startInterval = intervals[start]
        # endInterval = intervals[end]
        # print(f"start: {startInterval}")
        # print(f"end: {endInterval}")
        # # check if we should merge with an existing interval
        # if startInterval[0] <= newInterval[0] <= startInterval[1]:
        #     # merging with start of new interval
        #     # remove all intervals between start-end (exclusive)
        #     # remove from start + 1 to end inclusive
        #     startVal = min(startInterval[0], newInterval[0])
        #     endVal = max(endInterval[1], newInterval[1])
        #     intervals[start] = [startVal, endVal]
        #     removeRedundant(start)
        #     # check for redundant
        #     # [1,3],[4,6] [2,5] --> [1,6],[4,6]
        # # case merge with the ending interval
        
        # elif endInterval[0] <= newInterval[1] <= endInterval[1]:
        #     # iterate to start interval backwards (exclusive) remove all those nodes
        #     # remove from end - 1 to start (inclusive)
        #     # basically removing all nodes bigger than start since we're merging those
        #     startVal = min(startInterval[0], newInterval[0])
        #     endVal = max(endInterval[1], newInterval[1])
        #     intervals[end] = [startVal, endVal]
        #     removeRedundant(end)
        # else:
        #     # nothing is intersecting so just insert a new value at start
        #     intervals.insert(start + 1, newInterval)
        #     # or an easier way is to check whether the intervals going back are redundant
        #     # (already defined in this interval)

        # return intervals

        
        # # [1,2],[4,6],[8,10]   [5,11] 
        # # [1,2],[4,6][4,11]

            

        




