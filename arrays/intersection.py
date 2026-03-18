# class Solution(object):
#     def intersection(self, nums1, nums2):
#         set1 = set(nums1)
#         res = []
#         for num in nums2:
#             if num in set1:
#                 res.append(num)
#                 set1.remove(num) # Ensures each element in result is unique
#         return res
# # Example usage:
# solution = Solution()
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(solution.intersection(nums1, nums2))  # Output: [2]



def intersection(nums1,nums2):
    set1 = set(nums1)
    res = []
    for num in nums2:
        if num in set1:
            res.append(num)
            set1.remove(num) ## to ensure that each element in result is unique
        return res 
print(intersection([1,2,2,1],[2,2]))



