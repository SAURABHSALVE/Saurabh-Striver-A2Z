
def findNumbers(nums):
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
print(findNumbers([1,2,3,4,5])) # Output: 0
    