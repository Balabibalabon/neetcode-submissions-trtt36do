class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Result = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            num_1 = nums[i]
            left_P = i+1
            right_P = len(nums)-1
            while left_P < right_P:
                num_2 = nums[left_P]
                num_3 = nums[right_P]
                tmp = num_1 + num_2 + num_3
                if tmp < 0:
                    left_P += 1
                elif tmp > 0:
                    right_P -= 1
                else:
                    Result.append([num_1, num_2, num_3])
                    left_P += 1
                    right_P -= 1

                    while left_P < right_P and num_2 == nums[left_P]:
                            left_P+=1
                    while left_P < right_P and num_3 == nums[right_P]:
                            right_P-=1
        
        return Result
