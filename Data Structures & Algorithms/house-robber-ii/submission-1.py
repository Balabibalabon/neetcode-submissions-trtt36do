class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        # 排除最後一格
        prev_2 = nums[0]
        prev_1 = max(nums[0],nums[1])
        
        for i in range(2,n-1):
            cur_1 = max(prev_2 + nums[i], prev_1)
            prev_2 = prev_1
            prev_1 = cur_1
        o_1 = prev_1
        
        # 排除第一格
        prev_2 = nums[1]
        prev_1 = max(nums[1],nums[2])
        for i in  range(3,n):
            cur_2 = max(prev_2 + nums[i], prev_1)
            prev_2 = prev_1
            prev_1 = cur_2
        o_2 = prev_1

        return max(o_1, o_2)
            