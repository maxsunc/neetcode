"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # check for a n overlap between intervals
        # if there is overlap then we return false
        # to find overlap we can sort by start date 
        # keep track of the prevEnd and if our start is less than the prevEdn then we can return False
        intervals.sort(key=lambda x: x.start)

        prevEnd = -1

        for i,val in enumerate(intervals):
            if prevEnd > val.start:
                return False
            prevEnd = val.end
        return True