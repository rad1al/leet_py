class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
        return self.convertToBase7(num / 7) + str(num % 7)
    
    # c(12) = c(1) ++ c(5) = '15'
    # c(-7) = '-' ++ c(7) = '-7'
    # c(-12) = '-' ++ c(12) = '-15'
    # c(222) = c(31) ++ c(5) = (c(4) ++ c(3)) ++ c(5) = '435'