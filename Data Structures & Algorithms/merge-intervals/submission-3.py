class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # find the overlapping intervals and merge them
        # is it sorted?
        intervals.sort(key=lambda x: x[0])
        # keep a stack of elements and determine whether
        # constantly check whether we can merge the top vlaue of the stack (if there even is a top value)
        stack = []

        for i, interval in enumerate(intervals):
            if not stack:
                stack.append(interval)
            else:
                # stack has a top 
                top = stack[-1]
                # check if they overlap (prevEnd is greater than the start value)
                if interval[0] <= top[1]:
                    # overlapping so merge them
                    stack[-1][1] = max(stack[-1][1],interval[1])
                else:
                    # no overlap
                    stack.append(interval)
        return stack


