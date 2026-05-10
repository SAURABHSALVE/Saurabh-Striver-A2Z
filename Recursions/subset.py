class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums,[],0,result)
        return result


    def helper(self,nums,ans,i,result):
        if i == len(nums):
            result.append(ans[:])
            return
        ans.append(nums[i])
        self.helper(nums,ans,i+1,result)
        ans.pop()
        self.helper(nums,ans,i+1,result)


        