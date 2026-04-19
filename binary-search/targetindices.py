# class Solution(object):
#     def targetIndices(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 res.append(i)
        
#         return res
    
    
class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        n = len(nums)

        # Lower Bound: First index where nums[i] >= target
        def get_lower_bound(nums, target):
            low, high = 0, n
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Upper Bound: First index where nums[i] > target
        def get_upper_bound(nums, target):
            low, high = 0, n
            while low < high:
                mid = low + (high - low) // 2
                # The ONLY difference: we use <= instead of <
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        start = get_lower_bound(nums, target)
        end = get_upper_bound(nums, target)

        # All indices from start up to (but not including) end
        return list(range(start, end))