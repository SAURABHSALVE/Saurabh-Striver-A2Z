class Solution(object):
    def maxArea(self, height):
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate width (distance between pointers)
            width = right - left
            
            # The height of the water is limited by the shorter wall
            current_height = min(height[left], height[right])
            
            # Update the maximum area found so far
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Logic: Move the pointer that points to the SHORTER wall.
            # Why? Because moving the taller wall can only decrease the area 
            # (since width decreases and height is still limited by the shorter wall).
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
    
## examples
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(solution.maxArea([1,1]))  # Output: 1
