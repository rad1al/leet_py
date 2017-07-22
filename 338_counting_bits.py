class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(x)[2:].count('1') for x in range(num+1)]

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # O(n) solution using two pointers.
        lst = [0] * (num+1)
        power = 1
        t = 0
        for i in xrange(1, num+1):
            if i == power:
                power *= 2
                t = 0
            lst[i] = lst[t] + 1
            t += 1
        return lst
                
        