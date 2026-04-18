class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        dp = {}
        dp[len(nums)-1] = True

        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=len(nums) or nums[i] == 0:
                return False
            for s in range(nums[i],0,-1):
                n = s+i
                dp[n] = dfs(n)
                if dp[n]:
                    return True
            return False

        
        if dfs(0):
            return True
        return False