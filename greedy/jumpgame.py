class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxindex = 0 
        for i in range(len(nums)):
            if i > maxindex:
                return False
            maxindex = max(maxindex,i+nums[i])
        return True 

# Main driver code
if __name__ == "__main__":
    # Input data
    nums = [2,3,1,1,4]

    # Initialize solution and get results
    sol = Solution()
    res = sol.canJump(nums)
    
    # Expected output: True
    print(res)
    
    
    ### command to run is  python greedy/jumpgame.py
    