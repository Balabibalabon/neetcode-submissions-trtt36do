"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        room = []
        for i in intervals:
            if room and room[0]<=i.start:
                heapq.heappop(room)

            heapq.heappush(room, i.end)
        return len(room)