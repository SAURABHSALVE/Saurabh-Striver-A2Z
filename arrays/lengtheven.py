class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        n = len(nums)

        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                even += 1

        return even
print(Solution().findNumbers([12,345,2,6,7896]))
