class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_P = 0
        right_P = len(heights)-1
        Result = 0

        while left_P < right_P:
            area = min(heights[left_P], heights[right_P]) * (right_P-left_P)
            if area > Result:
                Result = area
            
            if heights[left_P] > heights[right_P]:
                right_P -= 1
            elif heights[left_P] < heights[right_P]:
                left_P += 1
            elif heights[left_P+1] > heights[right_P-1]:
                right_P -= 1
            else:
                left_P += 1
        return Result
