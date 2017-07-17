class Solution(object):
    squares = {x**2 for x in range(0,100000)}
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """        
        for x in self.squares:
            if (c - x) in self.squares:
                return True
        return False

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**0.5)**2 == N
            
        return any(is_square(c - a*a) for a in xrange(int(c**.5) + 1))    

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """ 
        # Likely O(sqrt(c)
        if c < 0:
            return False

        left = 0
        right = int(c**0.5);
        while left <= right:
            cur = left * left + right * right
            if cur < c:
                left += 1
            elif cur > c:
                right -= 1
            else:
                return True;
        return False;
    