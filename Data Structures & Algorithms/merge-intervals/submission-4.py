class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge all overlapping intervals and return an array of the non-overlapping intervals that cover all intervals in the input
        

        # they're not sorted intervals

        # sort the intervals by start vlaue

        # [[1,1000],[4,5],[3,1001]] = [[1,1001]]


        # have a stack: iterate through intervals:
        # foreach element 
        # if our stack is emptyjust append it
        # if its not empty check the top valiue of thestack 
        # does it overlap with the currentInterval? If it does then pop, merge
        # if it doesnt overlap then just break out of the loop and add
        intervals = sorted(intervals,  key=lambda x: x[0])
        stack = []

        for interval in intervals:
            # if not stack:
            #     stack.append(interval)
            #     continue
            
            newInterval = interval
            # insert interval into stack
            while stack:
                curInterval = stack[-1]
                if newInterval[0] <= curInterval[1]:
                    curInterval = stack.pop()
                    newInterval = [min(newInterval[0],curInterval[0]), max(newInterval[1],curInterval[1])]
                else:
                    break
            # append the newInterval 
            stack.append(newInterval)
        
        return stack
