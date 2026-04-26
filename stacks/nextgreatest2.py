class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize result array with -1
        nge = [-1] * n 
        stack = []
        
        # We simulate a circular array by traversing from 2*n - 1 down to 0
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]
            
            # Maintain a monotonic decreasing stack (top is the smallest)
            while stack and stack[-1] <= current:
                stack.pop()
            
            # We only fill the result array during the first 'n' indices (0 to n-1)
            if i < n:
                if stack:
                    nge[i] = stack[-1]
            
            # Push current element onto the stack for the next elements to see
            stack.append(current)
            
        return nge