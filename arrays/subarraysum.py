class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        current_sum = 0
        
        # Dictionary to keep track of how many times we've seen a specific prefix sum.
        # We start with {0: 1} to account for subarrays that start from the very beginning (index 0) and exactly equal k.
        prefix_sums = {0: 1}
        
        for num in nums:
            # Update our running total
            current_sum += num
            
            # Check if (current_sum - k) is in our dictionary
            # If it is, it means we found one (or more) valid subarrays ending at this exact number!
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # Record the current running total in our dictionary for future numbers to use
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
                
        return count

# Example usage:
solution = Solution()

nums = [1, 1, 1]
k = 2
print(solution.subarraySum(nums, k))  # Output: 2 (the subarrays [1, 1] at indices (0, 1) and (1, 2) both sum to 2)
