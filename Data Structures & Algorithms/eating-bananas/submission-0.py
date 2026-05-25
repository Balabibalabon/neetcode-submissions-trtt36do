import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            m = (l+r)//2
            t_h = 0
            for i in piles:
                t_h += math.ceil(i/m)
            
            if t_h <= h:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res