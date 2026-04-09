class Solution(object):
    def findMaxLength(self, nums):
        # Map: current_sum -> first index it appeared
        count_map = {0: -1}
        curr_sum = 0
        max_len = 0
        
        for i, n in enumerate(nums):
            # Change 0 to -1, 1 stays 1
            curr_sum += 1 if n == 1 else -1
            
            if curr_sum in count_map:
                # If we've seen this sum before, calculate distance
                max_len = max(max_len, i - count_map[curr_sum])
            else:
                # Only store the FIRST time we see a sum to keep it longest
                count_map[curr_sum] = i
                
        return max_len 
    
## examples
nums = [0, 1, 0, 1, 0]
print(Solution().findMaxLength(nums))  # Output: 4 (subarray [0, 1, 0, 1])
