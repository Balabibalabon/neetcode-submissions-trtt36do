class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        prev_2 = nums[0]
        prev_1 = max(nums[0],nums[1])
        for i in range(2,n):
            cur = nums[i] + prev_2
            res = max(prev_1, cur)
            prev_2 = prev_1
            prev_1 = res
            print("現在在看第",i+1,"格，目前兩格狀態為:",prev_2, prev_1)
        return res