class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        if amount < coins[0]:
            return -1

        dp = [int(10e9)] * (amount + 1)

        for i in coins:
            if i < amount:
                dp[i] = 1

        for i in range(coins[0], amount + 1):
            if i in coins:
                continue
            else:
                for j in coins:
                    if j < amount and i > j:
                        a = dp[i]
                        b = dp[i - j] + 1
                        dp[i] = min(a, b)

        if dp[amount] != int(10e9):
            return dp[amount]

        return -1