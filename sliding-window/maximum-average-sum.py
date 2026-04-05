class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0 
        j = 0 
        maxi = float('-inf')
        curr_sum = 0 
        while j < len(nums):
            curr_sum = curr_sum + nums[j]
            if j - i + 1 < k:
                j +=1 
            elif j - i + 1 == k:
                maxi = max(maxi,curr_sum)
                curr_sum -= nums[i]
                i+=1
                j+=1 
        return float(maxi)/k

## examples
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))  # Output: 12.75 (subarray [12, -5, -6, 50])  