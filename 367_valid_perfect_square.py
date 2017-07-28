class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: 
            return True
        guess = num >> 1
        while True:
            new_guess = self.newton(num, guess)
            if abs(new_guess - guess) < 1e-10:
                # return new_guess
                return abs(new_guess - round(new_guess)) < 1e-10
            guess = new_guess
        
    def newton(self, num, guess):
    	# Part of Newton's method, takes a guess for the square root 
    	# and returns a better guess.
	    return guess - (guess**2 - num)/(2.0 * guess)

