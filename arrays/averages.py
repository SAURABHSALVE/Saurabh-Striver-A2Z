class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        averages = set()  # Sets only store unique values
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            # Calculate the average of the values, not the indices
            avg = (nums[l] + nums[r]) / 2.0
            
            # Add to set (if it's already there, the set won't change)
            averages.add(avg)
            
            # Move pointers inward
            l += 1
            r -= 1
            
        # The number of distinct averages is simply the size of the set
        return len(averages)

print(Solution().distinctAverages([4,1,4,0,3,5]))  # Output: 2

"""
Given an array of integers nums, the average of a pair of elements (a, b) is (a + b) / 2.
The distinctAverages function should return the number of distinct averages that can be formed by pairing the elements of the array. Each element can only be used once in a pair.
Example 1: nums = [4,1,4,0,3,5], target = 3
Output: 2
Explanation: The pairs (1, 0) and (4, 3) have averages of 0.5 and 3.5 respectively.
"""