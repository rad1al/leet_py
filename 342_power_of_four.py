class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        b = bin(num)[2:]
        return b[0] == '1' and len(b[1:]) % 2 == 0 and all([x == '0' for x in b[1:]])