class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate the total sum of the array once upfront
        total_sum = sum(nums)
        
        # Keep a running total of the elements to the left of our current index
        left_sum = 0
        
        for i in range(len(nums)):
            # Check if the left side equals the right side
            # Right side is exactly: total_sum - left_sum - current number
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            
            # If it's not the pivot, add the current number to the left_sum 
            # so it's ready for the next iteration
            left_sum += nums[i]
            
        # If the loop finishes without returning, no pivot exists
        return -1
# Example usage:
solution = Solution()

nums = [1, 7, 3, 6, 5, 6]

print(solution.pivotIndex(nums))  # Output: 3 (index of the pivot element 6)
