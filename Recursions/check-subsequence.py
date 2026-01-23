class Solution:
    # This method recursively checks for the subsequence with the given sum
    def solve(self, i, n, arr, k):
        # Base case: if the sum k is 0, a subsequence is found
        if k == 0:
            return True
        # Base case: if k is negative, no valid subsequence can be found
        if k < 0:
            return False
        # Base case: if all elements are processed, check if k is 0
        if i == n:
            return k == 0
        
        # Recursive call: include the current element in the subsequence
        # or exclude the current element from the subsequence
        return self.solve(i + 1, n, arr, k - arr[i]) or self.solve(i + 1, n, arr, k)

    # This method initiates the recursive process
    def checkSubsequenceSum(self, nums, target):
        n = len(nums) # Get the length of the input array
        return self.solve(0, n, nums, target) # Start the recursive process

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    target = 5
    print(sol.checkSubsequenceSum(nums, target)) # Expected output: True
