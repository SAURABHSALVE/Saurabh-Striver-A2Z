class Solution(object):
    def minimumCost(self, nums):
        n = len(nums)

        # First subarray always starts at index 0
        first = nums[0]

        # Sort remaining elements
        rest = sorted(nums[1:])

        # Minimum cost = nums[0] + two smallest after it
        return first + rest[0] + rest[1]


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 12]
    print("Input:", nums1)
    print("Output:", sol.minimumCost(nums1))
    print()

    # Test Case 2
    nums2 = [5, 4, 3]
    print("Input:", nums2)
    print("Output:", sol.minimumCost(nums2))
    print()

    # Test Case 3
    nums3 = [10, 3, 1, 1]
    print("Input:", nums3)
    print("Output:", sol.minimumCost(nums3))
