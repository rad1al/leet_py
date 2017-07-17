class Solution(object):
    class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Use a(a+1)/2 = n
        # Solve for a in terms of n
        # Get quadratic equation of a^2 + a - 2k = 0
        # Solve for positive root: a = (-1 + sqrt(1+8k))/2
        # Find floor of result by casting to int.
        return int((-1 + (1+8*n)**0.5)/2)
        