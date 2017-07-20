class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        sub_strs = [s[i*k:(i+1)*k] for i in xrange((len(s)/k)+1)]
        result = list()
        for i, item in enumerate(sub_strs):
            if i % 2 == 0:
                result.append(item[::-1])
            else:
                result.append(item)
        return ''.join(result)