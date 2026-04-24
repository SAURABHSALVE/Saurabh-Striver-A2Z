class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # 1. Pre-allocate the list so we can use index assignment
        nge = [-1] * n 
        stack = []
        
        # 2. Iterate from 2n-1 down to 0 to simulate a circular array
        for i in range(2 * n - 1, -1, -1):
            # Use modulo to stay within array bounds
            current = nums[i % n]
            
            # Standard monotonic stack logic
            while stack and stack[-1] <= current:
                stack.pop()
            
            # 3. Only fill the result array during the "actual" first pass
            if i < n:
                if stack:
                    nge[i] = stack[-1]
                else:
                    nge[i] = -1
            
            stack.append(current)
            
        return nge