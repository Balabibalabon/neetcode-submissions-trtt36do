class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_dict = {} #key:number, value:count
        for i in nums:
            count_dict[i] = 1+ count_dict.get(i,0)
        print("count_dict:", count_dict)
        
        Result = list()
        for i in range(len(nums)):
            tmp = 1
            for key, value in count_dict.items():
                if key == nums[i]:
                    product_time = value-1
                else:
                    product_time = value
                tmp *= (key**product_time)
                print("key:", key, "value:", value, "乘上次數:", product_time, "tmp:", tmp)

            Result.append(tmp)
        return Result 
