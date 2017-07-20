class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_s = 0
        l_s = 0
        i = 0
        while i < len(s):
            if (s[i]) == 'L':
                l_s += 1
            else:
                l_s = 0
            if (s[i]) == 'A':
                a_s += 1                
            if a_s > 1 or l_s > 2:
                return False
            i += 1
        return True