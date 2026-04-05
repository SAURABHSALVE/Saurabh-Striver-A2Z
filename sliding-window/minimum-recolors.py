class Solution(object):
    def minimumRecolors(self, blocks, k):
        i = 0
        j = 0
        white_count = 0
        mini = float('inf')
        
        while j < len(blocks):
            # Add logic: if it's a White block, we might need to recolor it
            if blocks[j] == 'W':
                white_count += 1
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                # Update answer: we want the window with the LEAST white blocks
                mini = min(mini, white_count)
                
                # Subtract logic: remove the leftmost block from our count
                if blocks[i] == 'W':
                    white_count -= 1
                
                i += 1
                j += 1
        return mini
## examples
blocks = "WBBWWBBWBW"
k = 7
print(Solution().minimumRecolors(blocks, k))  # Output: 3 (subarray "BBWWBBW")
