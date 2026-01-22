class Solution(object):
    def subsets(self, nums):
        res = []
        curr = []

        def helper(i):
            if i == len(nums):
                res.append(curr[:])  # copy once per subset
                return

            # include
            curr.append(nums[i])
            helper(i + 1)

            # exclude
            curr.pop()
            helper(i + 1)

        helper(0)
        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.subsets([1, 2, 3])
    for subset in result:
        print(subset)