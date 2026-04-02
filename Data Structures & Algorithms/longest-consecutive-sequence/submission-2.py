class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 1
        Result = 0
        for i in nums:
            if i-1 not in nums_set:
                number = i
                while number+1 in nums_set:
                    count+=1
                    number+=1
                if count > Result:
                    Result = count
                count = 1
        return Result