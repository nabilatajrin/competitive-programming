#Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
#The time complexity is O(amount * coins.length) and the space complexity is O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
