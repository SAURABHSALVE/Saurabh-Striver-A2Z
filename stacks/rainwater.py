class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        leftmax = rightmax = 0 
        l,r = 0,len(height)-1
        total  = 0 
        while l < r:
            if height[l] <= height[r]:
                if leftmax > height[l]:
                    total += leftmax - height[l]
                else:
                    leftmax = height[l]
                l = l+1
            else:
                if rightmax > height[r]:
                    total += rightmax - height[r]
                else:
                    rightmax = height[r]
                r-=1
        return total
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))