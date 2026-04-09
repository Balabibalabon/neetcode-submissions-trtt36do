class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        count = 0
        def centerP(l,r):
            cnt = 0
            while l>=0 and r<n and s[l] == s[r]:
                cnt += 1
                l-=1
                r+=1
            return cnt   
        
        for i in range(n):
            count += centerP(i,i)
            count += centerP(i,i+1)
        return count