import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1 
        high = max(piles)
        ans = high # Start with the max possible speed
        
        while low <= high:
            mid = (low + high) // 2 
            # Use self. to call the helper method
            total_h = self.totalhours(piles, mid)
            
            if total_h <= h:
                ans = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        
        return ans

    def totalhours(self, piles, speed):
        total_hours = 0 
        for p in piles:
            # We use float division (/) so ceil can actually round up
            # Example: ceil(7 / 3) = 3.0
            total_hours += math.ceil(float(p) / speed)
        return total_hours
    