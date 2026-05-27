def coststairs(cost):
    n = len(cost)
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[n]
# Test cases
print(coststairs([10, 15, 20]))  # Output: 15
print(coststairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6
