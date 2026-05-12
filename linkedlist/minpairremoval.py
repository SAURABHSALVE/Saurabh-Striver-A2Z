class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        
        # Helper function to check if array is non-decreasing
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
            
        # Keep simulating until the array is sorted
        while not is_sorted(nums):
            min_sum = float('inf')
            min_index = -1
            
            # Find the adjacent pair with the minimum sum
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_index = i
                    
            # Replace the pair with their sum
            nums[min_index] = min_sum
            nums.pop(min_index + 1) # Remove the second element of the pair
            
            ans += 1
            
        return ans