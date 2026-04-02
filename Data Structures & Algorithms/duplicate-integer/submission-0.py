class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        if length==1:
            return False
        pointer = 0
        while(pointer<length and pointer+1<length):
            if(nums[pointer]==nums[pointer+1]):
                return True
            else:
                pointer +=1
        return False
