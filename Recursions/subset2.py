class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Mandatory for the skip logic to work
        nums.sort() 
        result = []
        self.helper(nums, [], 0, result)
        return result
    
    def helper(self, nums, ans, i, result):
        if i == len(nums):
            result.append(ans[:])
            return
        
        # 1. Pick (Your order)
        ans.append(nums[i])
        self.helper(nums, ans, i + 1, result)
        
        # 2. Skip logic (Your order)
        # We find the first index that is NOT a duplicate of nums[i]
        idx = i + 1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1 
            
        # 3. Pop (Your order)
        ans.pop()
        
        # 4. Don't Pick (The fix: use the 'idx' jump instead of 'i+1')
        self.helper(nums, ans, idx, result)