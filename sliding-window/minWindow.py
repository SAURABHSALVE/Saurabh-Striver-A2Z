class Solution(object):
    def minWindow(self, s, t):
        i = 0
        j = 0
        # 1. Map the 'debt' (what characters we need from t)
        hashmap = {}
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        # 'count' tracks how many unique characters in t still need to be satisfied
        count = len(hashmap)
        ans = ""
        min_len = float('inf')
        
        while j < len(s):
            # 2. Add logic: If s[j] is a character we need, reduce its debt
            if s[j] in hashmap:
                hashmap[s[j]] -= 1
                if hashmap[s[j]] == 0: # One character requirement fully met
                    count -= 1
            
            # 3. If count == 0, the window is VALID (contains all of t)
            while count == 0:
                # Update the smallest window found so far
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = s[i : j+1]
                
                # 4. Shrink logic: Try to make the window even smaller
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    # If the debt goes above 0, we no longer have a valid window
                    if hashmap[s[i]] > 0:
                        count += 1
                i += 1
            
            j += 1
            
        return ans
    