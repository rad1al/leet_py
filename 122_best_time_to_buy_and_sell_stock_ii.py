class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in xrange(len(prices)-1):
            if prices[i] < prices[i+1]:
                total += prices[i+1]-prices[i]
        return total

assert Solution().maxProfit([3,1,4,8]) == 7
assert Solution().maxProfit([2,3,1,4,8]) == 8
