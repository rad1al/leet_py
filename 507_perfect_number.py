import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum_ = 0
        n = 2
        while n < int(math.sqrt(num)+1):
            if num % n == 0:
                sum_ += n
                if n * n != num:
                    sum_ += num / n
            n += 1
        return (sum_ + 1) == num
    
    # Use Euclid-Euler Theorem: 2^(p-1)*(2^p-1) is an even perfect number if 2^p-1 is prime.
    perfect = [(1 << (p - 1)) * ((1 << p) - 1) for p in [2,3,5,7,13,17,19,31]]
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in self.perfect:
            if p == num:
                return True
        return False

assert Solution().checkPerfectNumber(6) == True
assert Solution().checkPerfectNumber(28) == True