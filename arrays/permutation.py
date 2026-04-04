class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # 1. Initialize frequency arrays for 'a'-'z' (all zeros)
        s1_count = [0] * 26
        window_count = [0] * 26

        # 2. Fill s1_count and the first window of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # 3. Check if the first window is a match
        if s1_count == window_count:
            return True

        # 4. Slide the window across s2
        for i in range(n1, n2):
            # Add the character entering the window on the right
            window_count[ord(s2[i]) - ord('a')] += 1
            # Remove the character leaving the window on the left
            window_count[ord(s2[i - n1]) - ord('a')] -= 1

            # Compare current window count with target count
            if s1_count == window_count:
                return True

        return False
    
## examples 
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))  # Output: True
