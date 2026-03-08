class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        i = 0  # Point to the last unique element found
        for j in range(1, len(nums)):
            # If we find a new unique value
            if nums[i] != nums[j]:
                i += 1           # Move to the next slot
                nums[i] = nums[j] # Update that slot with the new value
                
        return i + 1

# Testing the code
print(Solution().removeDuplicates([1, 1, 2, 2, 3, 4, 5]))