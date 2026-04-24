class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        
        # Iterate backwards through a virtual doubled array
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]
            
            # Pop elements that are smaller or equal to the current element
            while stack and stack[-1] <= current:
                stack.pop()
            
            # Only update the result during the first pass (actual indices)
            if i < n:
                if stack:
                    res[i] = stack[-1]
            
            # Add current element to stack for the next comparison
            stack.append(current)
            
        return res
