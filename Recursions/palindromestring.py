class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Clean the string first so we don't have to worry about spaces/punctuation
        # Example: "A man, a plan!" becomes "amanaplan"
        clean_s = "".join([char.lower() for char in s if char.isalnum()])
        
        # Step 2: Define our recursive helper function
        def check_recursively(text):
            # BASE CASE: If we've chopped the string down to 1 or 0 letters, we win!
            if len(text) <= 1:
                return True
            
            # If the first and last letters don't match, we fail immediately.
            if text[0] != text[-1]:
                return False
            
            # RECURSIVE STEP: Chop off the first [0] and last [-1] letters.
            # text[1:-1] gives us the string without the ends.
            # We call the function AGAIN with this smaller string.
            return check_recursively(text[1:-1])
            
        # Step 3: Start the recursion!
        return check_recursively(clean_s)
