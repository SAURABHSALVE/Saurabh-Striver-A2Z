### sliding-window-maximum.py without using deque approach is as follows: variable size windows


# from collections import deque

# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         i = 0 
#         j = 0 
#         res = []
#         maximum = deque() # This replaces your single 'maxi' variable
        
#         while j < len(nums):
#             # 1. Add logic: Remove any numbers smaller than nums[j] 
#             # from the back because they can never be the maximum now.
#             while maximum and nums[maximum[-1]] < nums[j]:
#                 maximum.pop()
            
#             maximum.append(j) # Store the index, not the value
            
#             if j - i + 1 < k:
#                 j += 1 
#             elif j - i + 1 == k:
#                 # 2. Update Answer: The front of the list is always the max
#                 res.append(nums[maximum[0]])
                
#                 # 3. Subtract logic: If the max index we are tracking 
#                 # is the one that is sliding out (index i), remove it.
#                 if maximum[0] == i:
#                     maximum.popleft()
                
#                 # 4. Slide
#                 i += 1
#                 j += 1 
                
#         return res




class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0 
        j = 0 
        maximum = [] # To store indices of potential maximums
        ans = []        # To store the final results
        
        while j < len(nums):
            # 1. Add logic: Remove numbers from back that are smaller than nums[j]
            # They can never be the maximum because nums[j] is newer and larger
            while len(maximum) > 0 and nums[maximum[-1]] < nums[j]:
                maximum.pop()
            
            maximum.append(j)
            
            if j - i + 1 < k:
                j += 1 
            elif j - i + 1 == k:
                # 2. Update Answer: The current max is always at the front
                ans.append(nums[maximum[0]])
                
                # 3. Subtract logic: If the max index is the one leaving the window
                if nums[maximum[0]] == nums[i]:
                    maximum.pop(0) # Remove from front
                
                # 4. Slide
                i += 1
                j += 1
                
        return ans