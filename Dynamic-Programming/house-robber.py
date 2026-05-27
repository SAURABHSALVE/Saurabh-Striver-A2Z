class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            # Either rob this house (nums[i] + grand-total) or skip it (prev total)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[n-1]

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))  # Output: 4
    print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12
    print(sol.rob([1]))  # Output: 1
    print(sol.rob([1, 2]))  # Output: 2