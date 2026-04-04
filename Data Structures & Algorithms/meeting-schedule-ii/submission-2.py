"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # count itself as one room
        intervals.sort(key=lambda x: x.start)

        # 2: store the prev end Value to compare
        res = 0
        # prevEnd = -1
        rooms = []
        
        # 3: Iterating thru intervals: For each interval
        for i,interval in enumerate(intervals):
                # update since our new time is interval.start
                # check if we can free up any rooms
            while rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            # add the value to a room
            heapq.heappush(rooms, interval.end)
                

            # its vlaid so lets update result
            res = max(res, len(rooms))
                
        # update prevEndValue to min endvlaue
        return res
        # if no overlap then just replace prev end value 
        # [(5,10),(8,12),(15,20),(0,40)]




