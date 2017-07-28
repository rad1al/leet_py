class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 2
        best = reduce(lambda x, y: x*y, self.break_into_factors(n, k))
        while True:
            k += 1
            result = reduce(lambda x, y: x*y, self.break_into_factors(n, k))
            if result < best:
                return best
            else:
                best = result
        
    def break_into_factors(self, n, k):
        q = n/k
        factors = [q] * k
        remainder = n - q*k
        while remainder > 0:
            factors[remainder] += 1
            remainder -= 1
        return factors

    # There exists a DP solution. Need to figure it out.
