class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Base cases
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        # Helper function: Your exact House Robber 1 logic
        def rob_linear(houses):
            size = len(houses)
            dp = [0] * size
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, size):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
                
            return dp[size-1]
        
        # Step 3 shortcut: Take the max of both possible scenarios
        skip_last_house = rob_linear(nums[:-1])  # From index 0 to n-2
        skip_first_house = rob_linear(nums[1:])  # From index 1 to n-1
        
        return max(skip_last_house, skip_first_house)
