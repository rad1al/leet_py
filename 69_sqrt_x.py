class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        guess = x >> 1
        while True:
            new_guess = self.newton(x, guess)
            if abs(new_guess - guess) < 1e-10:
                # return new_guess
                return int(new_guess)
            guess = new_guess
        
    def newton(self, num, guess):
    	# Part of Newton's method, takes a guess for the square root 
    	# and returns a better guess.
	    return guess - (guess**2 - num)/(2.0 * guess)