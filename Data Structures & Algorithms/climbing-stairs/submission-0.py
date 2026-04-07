class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        prev_2 = 1
        prev_1 = 2
        for i in range(2,n):
            cur = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = cur
        return cur