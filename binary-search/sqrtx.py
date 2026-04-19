class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
            
        low, high = 2, x // 2
        ans = 1 # 1 is the minimum for x >= 1
        
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid # Store the potential floor value
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
    
    
    