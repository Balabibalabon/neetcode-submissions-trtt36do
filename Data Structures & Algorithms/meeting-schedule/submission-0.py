"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        list_interval = []
        for i in intervals:
            s, e = i.start, i.end
            list_interval.append([s,e])
        list_interval.sort(key = lambda x:x[0])
        tmp = list_interval[0]
        for i in range(1,len(list_interval)):
            if list_interval[i][0] < tmp[1]:
                return False
            tmp = [list_interval[i][0],list_interval[i][1]]
        return True