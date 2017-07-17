class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = str(bin(num))[2:]
        return int(''.join(['1' if x == '0' else '0' for x in binary]), 2)

assert Solution().findComplement(5) == 2