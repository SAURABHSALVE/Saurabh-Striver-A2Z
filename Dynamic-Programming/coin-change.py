class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin>= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1
# Test cases
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Output: 3
print(solution.coinChange([2], 3))         # Output: -1
print(solution.coinChange([1], 0))         # Output: 0


        