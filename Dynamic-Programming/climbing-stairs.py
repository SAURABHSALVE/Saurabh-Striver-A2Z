class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n 
        dp = [0]*(n+1)
        dp[1] = 1 
        dp[2] = 2 
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        
# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # Output: 2
    print(sol.climbStairs(3))  # Output: 3
    print(sol.climbStairs(4))  # Output: 5
    print(sol.climbStairs(5))  # Output: 8
    