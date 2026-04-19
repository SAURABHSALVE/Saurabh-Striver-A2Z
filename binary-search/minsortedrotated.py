class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums)-1
        while low < high:
            mid = (low + high)//2

            if nums[mid]> nums[high]:
                low = mid + 1 
            else:
                high = mid

        return nums[low]

### run command is 
# python binary-search/minsortedrotated.py


### second version 

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums)-1
        while low < high:
            mid = (low + high)//2

            if nums[mid]> nums[high]:
                low = mid + 1 
            else:
                high = mid

        return low
    
    
    
#### third type of so;lution 

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums) - 1
        ans = float('inf')
        
        while low <= high:
            mid = (low + high) // 2
            
            # Optimization: If the current search range is already sorted,
            # nums[low] is the smallest in this range.
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break
                
            # If the left half is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1 # Look in the right (unsorted) half
            # If the right half is sorted
            else:
                ans = min(ans, nums[mid])
                high = mid - 1 # Look in the left (unsorted) half
                
        return ans