class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        nge = [-1]*n 
        stack = []
        for i in range(2  x x cc c          v         v v vv   *n-1,-1,-1):
            current = nums[i%n]
            while stack and stack[-1]<=current:
                stack.pop()
            if i < n:
                if stack:
                    nge[i] = stack[-1]
            
            stack.append(current)
        return nge 
### this is the code