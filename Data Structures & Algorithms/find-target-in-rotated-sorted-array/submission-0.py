class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            if target == nums[r]:
                return r
            elif target == nums[l]:
                return l
            elif target == nums[m]:
                return m
            #正常排序
            elif nums[l]<=nums[m] and nums[m]<=nums[r]:
                if target>nums[m]:
                    l = m+1
                else:
                    r=m-1
            #右半邊正常排序
            elif nums[l]>=nums[m] and nums[r]>=nums[m]:
                if target>nums[m] and target<nums[r]:
                    l = m+1
                else:
                    r = m-1
            #左半邊正常排序
            elif nums[l]<=nums[m] and nums[r]<=nums[m]: 
                if target<nums[m] and target>nums[l]:
                    r = m-1
                else:
                    l = m+1
            print("target為:",target)
            print("目前抓到的區間為:",nums[l:r])
        return -1