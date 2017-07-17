class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dct = {5**k : n//5**k for k in range(1, 15)}
        return sum(dct.values())
        
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        total = 0
        while True:
            if 5**k <= n:
                total += n//5**k
                k += 1
            else:
                return total