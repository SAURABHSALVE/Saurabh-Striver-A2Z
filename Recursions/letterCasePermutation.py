class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        
        def backtrack(index, current_string):
            # Base Case: If we've processed the whole string, save the result
            if index == len(s):
                results.append("".join(current_string))
                return
            
            char = s[index]
            
            if char.isalpha():
                # Path 1: Try lowercase
                current_string.append(char.lower())
                backtrack(index + 1, current_string)
                current_string.pop() # Undo choice (backtrack)
                
                # Path 2: Try uppercase
                current_string.append(char.upper())
                backtrack(index + 1, current_string)
                current_string.pop() # Undo choice (backtrack)
            else:
                # It's a digit: Only one path possible
                current_string.append(char)
                backtrack(index + 1, current_string)
                current_string.pop()

        backtrack(0, [])
        return results