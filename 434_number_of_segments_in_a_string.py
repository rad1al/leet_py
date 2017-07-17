class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
    def countSegments_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0
        for i in xrange(len(s)):
            if s[i] != ' ' and ((i == 0) or (' ' == s[i-1])):
                t += 1
        return t
        # Time complexity:  O(n)
        # Space complexity: O(1)