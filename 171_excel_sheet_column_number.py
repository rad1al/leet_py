class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Recursive implementation.
        if len(s) == 1: 
            return ord(s)-64
        else:
            return self.titleToNumber(s[:-1])*26 + self.titleToNumber(s[-1])
        
        def titleToNumber_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, item in enumerate(reversed(s)): 
            total += 26**(i)*(ord(item)-64)
        return total

assert Solution().titleToNumber('AA') == 27