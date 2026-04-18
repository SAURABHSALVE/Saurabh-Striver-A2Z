class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums) - 1 
        n = len(nums)
        
        while low <= high:
            mid = (low + high) // 2 
            
            # Handle boundaries by using -infinity
            if mid > 0:
                left = nums[mid-1]
            else:
                left = float('-inf')
                
            if mid < n - 1:
                right = nums[mid+1]
            else:
                right = float('-inf')
            
            # 1. PEAK FOUND: nums[mid] is greater than both neighbors
            if left < nums[mid] > right: 
                return mid 
            
            # 2. UPHILL: We are climbing, so the peak must be to the right
            elif left < nums[mid] < right:
                low = mid + 1
            
            # 3. DOWNHILL or VALLEY: The peak is to the left
            else:
                high = mid - 1
        
        return low # Fallback
    
