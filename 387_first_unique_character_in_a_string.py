class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = dict()
        for l in s:
            if l not in dct:
                dct[l] = 1
            else:
                dct[l] += 1
        unique = {k for k in dct if dct[k] == 1}
        for i, item in enumerate(s):
            if item in unique:
                return i
        return -1