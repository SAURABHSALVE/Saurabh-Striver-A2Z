class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0 
        j = 0 
        maxi = 0 
        curr_vowels = 0
        vowels = "aeiou"
        while  j < len(s):
            if s[j] in vowels:
                curr_vowels += 1 
            if j - i + 1 < k:
                j +=1 
            elif j - i + 1 == k:
                maxi = max(maxi,curr_vowels)
                if s[i] in vowels:
                    curr_vowels -=1
                
                i +=1 
                j +=1
        return maxi 

## examples
s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))  # Output: 3 (subarray "iii")