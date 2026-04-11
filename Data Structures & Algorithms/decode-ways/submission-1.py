class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp.keys():
                return dp[i]
            if s[i] == "0":
                return 0

            dp[i] = dfs(i+1)
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dfs(i+2)

            return dp[i]
        return dfs(0)