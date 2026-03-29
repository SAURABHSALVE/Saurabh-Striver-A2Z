class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                # Swap current element with the left pointer
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                # Swap current element with the right pointer
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # Notice we DO NOT increment 'i' here, because the swapped 
                # number coming from the right hasn't been evaluated yet.
            else:
                # If nums[i] == 1, it's in the right place, just move forward
                i += 1
                
## example usage
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

## command to run this file
# python sortcolors.py
