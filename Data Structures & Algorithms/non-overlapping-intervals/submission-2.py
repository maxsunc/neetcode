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
        # # [[1,2],[2,4]]
        # def overlap(i1,i2): # i1 is within i2?
        #     return (i2[0] < i1[0] < i2[1]) or (i2[0] < i1[1] < i2[1]) or (i1[0] < i2[0] < i1[1]) or (i1[0] < i2[1] < i1[1]) or i1 == i2
        # 2. iterate with a stack comparing for overlap in values
        prevEndValue = -1
        res = 0
        for i, interval in enumerate(intervals):
        # 3. in overlap case between 2 intervals: Remove the interval with largest endValue
            if prevEndValue == -1:
                # stack.append(interval)
                prevEndValue = interval[1]
            else:
                # check whether the start value of this interval is less than the end value
                if prevEndValue > interval[0]:
                    # remov ethe vlaue with the end value
                    if prevEndValue > interval[1]:
                        prevEndValue = interval[1] # keep the smaller value
                    # else dont update since interval2 is smaller and we 'remove' intervla1
                    res += 1
                else:
                    # its good and lets update to new curINterval
                    prevEndValue = interval[1]
        return res





