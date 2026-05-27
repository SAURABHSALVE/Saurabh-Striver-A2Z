def climbing_stairs(n):
    if n <= 2:
        return n 
    dp = [0]*(n+1)
    dp[1] = 1 
    dp[2] = 2 
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
print(climbing_stairs(5))  # Output: 8
print(climbing_stairs(10)) # Output: 89