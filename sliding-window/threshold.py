class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        i = 0 
        j = 0 
        curr_sum = 0
        final_count = 0 
        
        while j < len(arr):
            curr_sum += arr[j]
            
            if j - i + 1 < k:
                j += 1 
            elif j - i + 1 == k:
                # Calculate the average and compare to threshold
                # Tip: curr_sum / k >= threshold is the same as curr_sum >= threshold * k
                if curr_sum / k >= threshold:
                    final_count += 1
                
                # Slide the window: subtract the outgoing element
                curr_sum -= arr[i]
                
                i += 1
                j += 1
                
        return final_count
## examples
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(Solution().numOfSubarrays(arr, k, threshold))  # Output: 3 (subarrays [2, 5, 5], [5, 5, 8], [5, 8, 8])