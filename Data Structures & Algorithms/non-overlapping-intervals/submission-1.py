class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals

        # intervals are not sorted
        #[1,2][2,3] are not overlapping

        # [[1,4],[1,2],[2,4],]

        # greedy: Remove the itnerval with the largest range 
        # [1,2] and [1,4] are overlapping
        # we need to remove either one of them
        # remove the one with larger endValue [1,4]

        # 1. sort in 1ascending order
        intervals.sort(key=lambda x: x[0])
        # [[1,2],[2,4]]
        def overlap(i1,i2): # i1 is within i2?
            return (i2[0] < i1[0] < i2[1]) or (i2[0] < i1[1] < i2[1]) or (i1[0] < i2[0] < i1[1]) or (i1[0] < i2[1] < i1[1]) or i1 == i2
        # 2. iterate with a stack comparing for overlap in values
        curInterval = []
        res = 0
        for i, interval in enumerate(intervals):
        # 3. in overlap case between 2 intervals: Remove the interval with largest endValue
            if len(curInterval) == 0:
                # stack.append(interval)
                curInterval = interval
            else:
                interval2 = curInterval
                # check whether interval is in interval 2
                if overlap(interval, interval2):
                    print(f"overlapping {interval} with {interval2}")
                    # remov ethe vlaue with the end value
                    if interval2[1] > interval[1]:
                        # remove interval 2 and add interval 1
                        curInterval = interval
                    # else dont update since interval2 is smaller and we 'remove' intervla1
                    res += 1
                else:
                    # its good and lets update to new curINterval
                    curInterval = interval
        return res





