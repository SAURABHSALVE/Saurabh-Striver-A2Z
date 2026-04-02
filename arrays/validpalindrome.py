import re 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## make the strings in lowercase
        s = s.lower()
        s= ''.join([char for char in s if char.isalnum()])
        if s[::-1] == s:
            return True 
        return False 
        
        



## examples
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
