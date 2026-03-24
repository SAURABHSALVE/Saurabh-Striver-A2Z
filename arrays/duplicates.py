class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        seen = set()

        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

# Example usage:
solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))  # Output: True
print(solution.containsDuplicate([1,2,3,4]))  # Output: False
