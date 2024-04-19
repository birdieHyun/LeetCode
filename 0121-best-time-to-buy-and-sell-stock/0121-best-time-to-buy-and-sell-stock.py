class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0] * len(prices)
        buy = prices[0]

        for i in range(1, len(prices)):
            dp[i] = prices[i] - buy
            buy = min(buy, prices[i])

        return max(dp)