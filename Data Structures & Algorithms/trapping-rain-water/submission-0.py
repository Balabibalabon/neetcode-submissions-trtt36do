class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        leftmax, rightmax = height[l], height[r]
        while l<r:
            if leftmax<=rightmax:
                i = l
                if leftmax-height[i]:
                    res+=leftmax-height[i]
                l+=1
                if height[l]>leftmax:
                    leftmax = height[l]
                # leftmax = max(leftmax, height[l])
                # res+= leftmax-height[l]
            else:
                i = r
                if rightmax - height[i]:
                    res += rightmax - height[i]
                r-=1
                if height[r]>rightmax:
                    rightmax = height[r]
        return res
            
        