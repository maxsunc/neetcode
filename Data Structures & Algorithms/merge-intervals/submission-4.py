class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # stack check if we can merge wit hthe most recent value.
        # we can only merge if theres an intersection
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        stack = []

        for i,interval in enumerate(intervals):
            if not stack:
                stack.append(interval)
            else:
                topVal = stack[-1][1]
                topVal2 = interval[1]
                if interval[0] <= topVal <= interval[1]  or stack[-1][0] <= topVal2 <= stack[-1][1]:
                    # merge
                    stack[-1] = [min(interval[0],stack[-1][0]),max(interval[1], stack[-1][1])]
                else:
                    # append as normal since no overlap
                    stack.append(interval)
        
        return stack

