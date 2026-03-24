class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        seen = set()
        
        for i in range(len(nums)):
            
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
            
            # Maintain window size k
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False

# Example usage:
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))  # Output: True
print(solution.containsNearbyDuplicate([1,0,1,1], 1))  # Output: True
