class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        res = []
        tmp = newInterval
        if newInterval[0] > intervals[-1][1]:
            for i in intervals:
                res.append(i)
            res.append(newInterval)
            return res
        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            for i in intervals:
                res.append(i)
            return res
        for s, e in intervals:
            print("現在 tmp 是:",tmp)
            print("s,e為:",s, e)
            if tmp:
                if (s<=tmp[0] and tmp[0]<=e) or (s<=tmp[1] and tmp[1]<=e):
                    tmp = [min(s,tmp[0]),max(e,tmp[1])]
                elif tmp[0]<s and tmp[1]>e:
                    pass
                elif s<tmp[0]:
                    res.append([s,e])
                else:
                    res.append(tmp)
                    tmp = [s,e]
            else:
                res.append([s,e])
            print("res為", res)
        if tmp:
            res.append(tmp)
        return res

