class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Two-pointer requires sorting
        count = 0 
        l = 0 
        r = len(nums) - 1 
        
        while l < r:
            curr_sum = nums[l] + nums[r]
            
            if curr_sum < target:
                # If nums[l] + nums[r] < target, then nums[l] paired with 
                # ANY index from l+1 to r will also be < target.
                count += (r - l)
                l += 1  # Move left pointer to try a new base number
            else:
                # Sum is too large, move the right pointer down to reduce it
                r -= 1
                
        return count
    