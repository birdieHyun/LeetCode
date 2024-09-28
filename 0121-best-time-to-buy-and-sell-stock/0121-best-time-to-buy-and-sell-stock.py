class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            result = prices[i] - buy
            answer = max(result, answer)

            if result < 0:
                buy = prices[i]
        return answer
