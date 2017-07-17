class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        return all([True if x == '0' else False for x in bin(n)[3:]])

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = float(n)
        while True: 
            if res == 1:
                return True
            elif res < 1:
                return False
            res /= 2