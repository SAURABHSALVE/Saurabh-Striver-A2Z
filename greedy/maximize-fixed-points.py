import bisect

class Solution(object):
    def maxFixedPoints(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Collect valid candidates as tuples: (d_i, nums[i])
        # where d_i is the number of required deletions (i - nums[i])
        valid_pairs = []
        for i, v in enumerate(nums):
            if v <= i:
                valid_pairs.append((i - v, v))
                
        # Sort primarily by required deletions (ascending)
        # Secondarily by the value itself (ascending)
        valid_pairs.sort()
        
        # Find the Longest Strictly Increasing Subsequence (LIS) on the values
        # We use bisect_left to ensure the sequence is STRICTLY increasing
        tails = []
        for d, v in valid_pairs:
            pos = bisect.bisect_left(tails, v)
            if pos == len(tails):
                tails.append(v)
            else:
                tails[pos] = v
                
        return len(tails)