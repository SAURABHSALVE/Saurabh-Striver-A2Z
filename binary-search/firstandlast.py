class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return [-1, -1]
        lb = self.lower(nums,target)

        if lb == n or nums[lb] != target:
            return [-1,-1]
        ub = self.upper(nums,target)
        
        return [lb,ub-1]
        



    def lower(self,nums,x):
        low = 0 
        high = len(nums)-1
        ans = len(nums)
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=x:
                ans = mid 
                high = mid -1 
            else:
                low = mid +1
        return ans
    def upper(self,nums,x):
        low = 0 
        high= len(nums)-1
        ans = len(nums)
        while low <=high:
            mid = (low +high)//2 
            if nums[mid ]> x:
                ans = mid 
                high = mid -1 
            else:
                low = mid +1
        return ans



        