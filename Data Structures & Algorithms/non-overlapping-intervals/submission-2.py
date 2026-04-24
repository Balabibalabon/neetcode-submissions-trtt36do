class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        n = len(intervals)
        prev = intervals[0]
        count = 0
        for i in range(1,n):
            s, e = intervals[i]
            if s>= prev[0] and s< prev[1]:
                if e<prev[1]:
                    prev = [s,e]
                count+=1
            else:
                prev = [s,e]
        return count
        