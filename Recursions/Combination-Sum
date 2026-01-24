class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        self.func(0, target, candidates, [], res)
        return res

    def func(self, i, target, candidates, path, res):
        # Base case
        if target == 0:
            res.append(path[:])
            return
        
        if i == len(candidates) or target < 0:
            return
        
        # Take (stay at same index because we can reuse element)
        path.append(candidates[i])
        self.func(i, target - candidates[i], candidates, path, res)
        path.pop()
        
        # Skip (move to next index)
        self.func(i + 1, target, candidates, path, res)
# Example usage:
sol = Solution()  
print(sol.combinationSum([2,3,6,7], 7))  # Output: [[7], [2,2,3]]

