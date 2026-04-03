class Solution(object):
    def characterReplacement(self, s, k):
        count = {} # Frequency map for characters in the window
        l = 0
        max_freq = 0
        max_len = 0
        
        for r in range(len(s)):
            # 1. Expand: Add the new character to the count
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # 2. Update max_freq: What is the most common char in the current window?
            max_freq = max(max_freq, count[s[r]])
            
            # 3. Check Validity: If (size - max_freq) > k, it's impossible. Shrink!
            # We use an 'if' instead of 'while' here because we only move 'l' 
            # by one to keep the window size from growing further.
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            # 4. Update the global maximum length found so far
            max_len = max(max_len, r - l + 1)
            
        return max_len
    
