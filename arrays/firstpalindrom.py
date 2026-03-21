class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
    
        for word in words:
            if word == word[::-1]:
                return word
        
        return ""
        
        
# Example usage:
solution = Solution()   

words = ["abc","car","ada","racecar","cool"]
print(solution.firstPalindrome(words))  # Output: "ada"
