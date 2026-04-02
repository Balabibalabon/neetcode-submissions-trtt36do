class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_P = 0
        right_P = 1
        Result = 0
        while right_P < len(prices):
            if prices[right_P] > prices[left_P]:
                profit = prices[right_P] - prices[left_P]
                Result = max(Result, profit)
            else:
                left_P = right_P
            right_P += 1
        return Result 