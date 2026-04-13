class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minR = 1
        maxR = 1
        res = nums[0]
        
        for n in nums:
            tmp = maxR
            maxR = max(n*maxR, n*minR, n)
            minR = min(n*tmp, n*minR, n)
            res = max(res, maxR)
        return res