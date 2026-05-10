class Solution(object):
    def minCost(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)

        # Step 1: Compute closest(i) for every index
        closest = [0] * n
        closest[0] = 1
        closest[n - 1] = n - 2
        for i in range(1, n - 1):
            left_diff = nums[i] - nums[i - 1]
            right_diff = nums[i + 1] - nums[i]
            # Strictly less → right is closer; otherwise left (smaller index on tie)
            closest[i] = i + 1 if right_diff < left_diff else i - 1

        # Step 2: For each consecutive boundary i↔i+1, compute min crossing cost
        # edge_right[i] = min cost to go from index i   → i+1
        # edge_left[i]  = min cost to go from index i+1 → i
        edge_right = [0] * (n - 1)
        edge_left  = [0] * (n - 1)

        for i in range(n - 1):
            gap = nums[i + 1] - nums[i]
            edge_right[i] = 1   if closest[i]     == i + 1 else gap
            edge_left[i]  = 1   if closest[i + 1] == i     else gap

        # Step 3: Build prefix sums for O(1) range queries
        prefix_right = [0] * n
        prefix_left  = [0] * n
        for i in range(1, n):
            prefix_right[i] = prefix_right[i - 1] + edge_right[i - 1]
            prefix_left[i]  = prefix_left[i - 1]  + edge_left[i - 1]

        # Step 4: Answer each query
        ans = []
        for l, r in queries:
            if l == r:
                ans.append(0)
            elif l < r:
                ans.append(prefix_right[r] - prefix_right[l])
            else:
                ans.append(prefix_left[l] - prefix_left[r])

        return ans