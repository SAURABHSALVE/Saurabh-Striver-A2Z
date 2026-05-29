class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0 
        if n==1 or n==2:
            return 1 
        dp = [0]*(n+1)
        dp[0] = 0 
        dp[1] = 1 
        dp[2] = 1 
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2] +dp[i-3]
        return dp[n]
# Time Complexity: O(n)
# Space Complexity: O(n)

## test cases 
s = Solution()
print(s.tribonacci(4)) # 2
print(s.tribonacci(25)) # 1389537

## command to run the code
# python Dynamic-Programming/n-th-tribonacci-number.py