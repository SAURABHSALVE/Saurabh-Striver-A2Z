class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum = 0
        i = 0 
        j = 0
        current_sum = 0
        window_elements = set() # To track uniqueness
        
        while j < len(nums):
            # If nums[j] is a duplicate, slide 'i' until it's not
            while nums[j] in window_elements:
                window_elements.remove(nums[i])
                current_sum -= nums[i]
                i += 1
            
            # Add current element
            current_sum += nums[j]
            window_elements.add(nums[j])
            
            # Check if window is the right size
            if j - i + 1 < k:
                j += 1 
            elif j - i + 1 == k:
                max_sum = max(max_sum, current_sum)
                
                # Slide the window: remove the leftmost element
                window_elements.remove(nums[i])
                current_sum -= nums[i]
                i += 1
                j += 1
                
        return max_sum

## examples
nums = [1, 2, 3, 4, 5]  
k = 3
print(Solution().maximumSubarraySum(nums, k))  # Output: 12 (subarray [3, 4, 5])