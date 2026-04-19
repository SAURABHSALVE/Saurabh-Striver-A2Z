class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identify the sorted half
            # Case 1: The left side is sorted
            if nums[left] <= nums[mid]:
                # Is the target inside this sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Case 2: The right side must be sorted
            else:
                # Is the target inside this sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1