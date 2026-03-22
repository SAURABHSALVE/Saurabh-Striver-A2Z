class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]   ## we will keep track of the minimum price we have seen so far and the maximum profit we can get by selling at the current price and buying at the minimum price.

        res = 0

        for i in range(1,len(prices)):

            mini = min(mini,prices[i]) ## update the minimum price if the current price is lower than the minimum price we have seen so far.

            res =  max(res , prices[i] - mini) ## update the maximum profit if the current profit is higher than the maximum profit we have seen so far.
        
        return res 
        


        