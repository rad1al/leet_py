import collections

class Solution(object):
    def findTheDifference_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_lst = list(t)
        for item in s:
            t_lst.remove(item)
        return [x for x in t_lst][0]

     def findTheDifference_2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list((collections.Counter(t) - collections.Counter(s)))[0]

    def findTheDifference_3(self, s, t):
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)

    def findTheDifference_4(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(lambda x, y: x ^ y, map(ord, s+t)))
