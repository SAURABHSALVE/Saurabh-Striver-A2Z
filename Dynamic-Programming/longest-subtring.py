class Solution(object):
    def longestPalindrome(self, s):
        longest = ""  # This will store our ultimate winner
        
        # Helper function goes inside here so it can read string 's'
        def expandFromCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        # Your loop that goes through every possible center
        for i in range(len(s)):
            # Case 1: Check for odd-length palindromes (center is a single letter)
            palindrome1 = expandFromCenter(i, i)
            
            # Case 2: Check for even-length palindromes (center is between two letters)
            palindrome2 = expandFromCenter(i, i + 1)
            
            # Now, update our 'longest' winner if either of these is bigger!
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
                
        return longest