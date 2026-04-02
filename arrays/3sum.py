class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort() # Step 1: Sort the array - O(n log n)
        
        for i in range(len(nums)):
            # Step 2: Skip duplicate "anchors"
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Two Pointers for the remaining part of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1 # Sum too large, move right pointer left
                elif three_sum < 0:
                    l += 1 # Sum too small, move left pointer right
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Step 4: Skip duplicate values for the left pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return res
## examples
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0,1,1]))  # Output: []
print(solution.threeSum([0,0,0]))  # Output: [[0, 0, 0]]