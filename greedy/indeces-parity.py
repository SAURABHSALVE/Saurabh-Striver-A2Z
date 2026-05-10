class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        # 1. Loop through each index in the array
        for i in range(len(nums)):
            count = 0
            
            # 2. Check every index 'j' that comes AFTER index 'i'
            for j in range(i + 1, len(nums)):
                
                # 3. Check if the parities are different. 
                # (Even % 2 is 0, Odd % 2 is 1. If they aren't equal, they are opposites!)
                if nums[i] % 2 != nums[j] % 2:
                    count += 1
            
            # 4. Add the final count for this index to our result
            res.append(count)
            
        return res