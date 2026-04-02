class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dotry(nums, 0, target, [])
        return self.res

    def dotry(self, nums, index, target, tmp=[]):
        if target == 0:
            self.res.append(tmp)
            return
        if index >= len(nums) or target < 0:
            return

        # Option 1: Skip the current number
        self.dotry(nums, index + 1, target, tmp.copy())
        
        # Option 2: Use the current number
        new_tmp = tmp.copy()
        new_tmp.append(nums[index])
        self.dotry(nums, index, target - nums[index], new_tmp)