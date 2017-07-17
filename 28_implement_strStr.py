class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in xrange(len(haystack)-(len(needle)-1)):
            if all([haystack[i+j] == needle[j] for j in xrange(len(needle))]):
                return i
        else:
            return -1
        # likely time complexity is O(M * N) where M is the length of haystack and N is the length of the needle

    def strStr_2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in xrange(len(haystack)-(len(needle)-1)):
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        else:
            return -1