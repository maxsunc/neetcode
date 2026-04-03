"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # scan for overlaps
        # its not sorted
        intervals.sort(key=lambda x: x.start)
        prevEndTime = -1

        for interval in intervals:
            if prevEndTime == -1:
                prevEndTime = interval.end
            else:
                # compare the prevEndTime with the start time
                if interval.start >= prevEndTime: # start >= prevEnd
                    # its good [0,20],[20,40]
                    prevEndTime = interval.end
                else:
                    return False
        return True
