class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor = n
        
        for i in range(n):
            xor ^= i
            xor ^= nums[i]
            
        return xor
print(Solution().missingNumber([3,0,1])) ## final answer
