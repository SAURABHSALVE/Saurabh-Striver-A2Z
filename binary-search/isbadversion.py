# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        while low < high:
            # Prevent potential overflow in some languages, 
            # though Python handles large integers automatically.
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is mid or to the left.
                # So we narrow the search to [low, mid].
                high = mid
            else:
                # If mid is good, the first bad version must be to the right.
                # So we narrow the search to [mid + 1, high].
                low = mid + 1
        
        # When the loop ends, low == high, which is the first bad version.
        return low

