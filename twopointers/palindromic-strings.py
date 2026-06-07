class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.total_count = 0  # To track total palindromes found
        
        def expandAndCount(l, r):
            count = 0
            # Keep expanding as long as characters match and inside bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1  # We found a valid palindrome! Count it!
                l -= 1      # Expand outward
                r += 1      # Expand outward
            return count

        # Loop through every single index as a potential center
        for i in range(len(s)):
            # Case 1: Odd length centers (e.g., "a", "b", "c")
            self.total_count += expandAndCount(i, i)
            
            # Case 2: Even length centers (e.g., "aa", "bb")
            self.total_count += expandAndCount(i, i + 1)
            
        return self.total_count
# Example usage:
solution = Solution()
print(solution.countSubstrings("abc"))  # Output: 3 (a, b, c)
print(solution.countSubstrings("aaa"))  # Output: 6 (a, a, a, aa, aa, aaa)