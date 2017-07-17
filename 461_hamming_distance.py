class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = '{0:032b}'.format(x)
        y_bin = '{0:032b}'.format(y)
        return sum([x_bin[i] != y_bin[i] for i, item in enumerate(x_bin)])