class Solution:
    def func(self,ind,remains,nums):
        if ind == len(nums):
            return 1 if remains == 0 else 0
        if remains < 0:
            return 0 

        ## take 
        take = self.func(ind + 1,remains - nums[ind], nums)
        skip = self.func(ind + 1,remains,nums)
    def count(self,nums,target):
        return self.func(0,nums,target)

    