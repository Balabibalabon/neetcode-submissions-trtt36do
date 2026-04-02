class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_P = 0
        right_P = 1
        Result = 0
        while right_P < len(prices):
            profit = prices[right_P] - prices[left_P]
            Result = max(Result, profit)
            if prices[right_P] < prices[left_P]:
                left_P = right_P
            right_P += 1
        return Result 